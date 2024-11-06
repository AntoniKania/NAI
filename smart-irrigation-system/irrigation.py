import pygame
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

WHITE = (255, 255, 255)
DARK_BLUE = (0, 102, 204)
LIGHT_GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100)
BLUE = (0, 128, 255)


def initialize_pygame():
    """Initialize Pygame and set up main colors, clock, and screen."""
    pygame.init()
    colors = {
        'WHITE': (255, 255, 255),
        'DARK_BLUE': (0, 102, 204),
        'LIGHT_GREY': (200, 200, 200),
        'DARK_GREY': (100, 100, 100),
        'BLUE': (0, 128, 255)
    }
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    return screen, clock, colors


def setup_fuzzy_system():
    """Define fuzzy variables, memberships, and control rules for the irrigation system."""
    soil_moisture_range = np.arange(0, 101, 1)
    rain_intensity_range = np.arange(0, 51, 1)
    temperature_range = np.arange(-10, 41, 1)
    irrigation_volume_range = np.arange(0, 51, 1)

    soil_moisture = ctrl.Antecedent(soil_moisture_range, 'soil_moisture')
    rain_intensity = ctrl.Antecedent(rain_intensity_range, 'rain_intensity')
    temperature = ctrl.Antecedent(temperature_range, 'temperature')
    irrigation_volume = ctrl.Consequent(irrigation_volume_range, 'irrigation_volume')

    soil_moisture['dry'] = fuzz.trapmf(soil_moisture_range, [0, 0, 20, 30])
    soil_moisture['optimal'] = fuzz.trapmf(soil_moisture_range, [20, 40, 60, 70])
    soil_moisture['wet'] = fuzz.trapmf(soil_moisture_range, [60, 70, 100, 100])

    rain_intensity['none'] = fuzz.trapmf(rain_intensity_range, [0, 0, 5, 10])
    rain_intensity['light'] = fuzz.trimf(rain_intensity_range, [5, 15, 25])
    rain_intensity['moderate'] = fuzz.trimf(rain_intensity_range, [20, 30, 40])
    rain_intensity['heavy'] = fuzz.trapmf(rain_intensity_range, [30, 40, 50, 50])

    temperature['cold'] = fuzz.trapmf(temperature_range, [-10, -10, 5, 15])
    temperature['moderate'] = fuzz.trapmf(temperature_range, [10, 20, 25, 30])
    temperature['hot'] = fuzz.trapmf(temperature_range, [25, 30, 40, 40])

    irrigation_volume['none'] = fuzz.trimf(irrigation_volume_range, [0, 0, 5])
    irrigation_volume['small'] = fuzz.trimf(irrigation_volume_range, [5, 10, 20])
    irrigation_volume['medium'] = fuzz.trimf(irrigation_volume_range, [15, 25, 35])
    irrigation_volume['large'] = fuzz.trapmf(irrigation_volume_range, [30, 40, 50, 50])

    rules = [
        ctrl.Rule(soil_moisture['dry'] & temperature['hot'], irrigation_volume['large']),
        ctrl.Rule(soil_moisture['dry'] & temperature['moderate'], irrigation_volume['medium']),
        ctrl.Rule(soil_moisture['dry'] & temperature['cold'], irrigation_volume['small']),
        ctrl.Rule(soil_moisture['optimal'] & temperature['hot'], irrigation_volume['medium']),
        ctrl.Rule(soil_moisture['optimal'] & temperature['cold'], irrigation_volume['none']),
        ctrl.Rule(soil_moisture['optimal'] & temperature['moderate'], irrigation_volume['small']),
        ctrl.Rule(soil_moisture['optimal'] & rain_intensity['moderate'], irrigation_volume['small']),
        ctrl.Rule(rain_intensity['moderate'] & temperature['hot'], irrigation_volume['small']),
        ctrl.Rule(rain_intensity['light'] & temperature['hot'], irrigation_volume['medium']),
        ctrl.Rule(rain_intensity['none'] & temperature['moderate'], irrigation_volume['small']),
        ctrl.Rule(rain_intensity['heavy'] & soil_moisture['wet'], irrigation_volume['none']),
        ctrl.Rule(rain_intensity['heavy'], irrigation_volume['none']),
        ctrl.Rule(soil_moisture['wet'], irrigation_volume['none']),
        ctrl.Rule(soil_moisture['optimal'], irrigation_volume['small']),
        ctrl.Rule(rain_intensity['heavy'] & temperature['cold'], irrigation_volume['none'])
    ]

    irrigation_ctrl = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(irrigation_ctrl)


def draw_slider(screen, label, x, y, current_value, min_value, max_value, colors):
    """Draw a slider with label and current value on the screen."""
    pygame.draw.line(screen, colors['LIGHT_GREY'], (x, y), (x + 100, y), 5)
    handle_x = x + int((current_value - min_value) / (max_value - min_value) * 100)
    pygame.draw.circle(screen, colors['DARK_BLUE'], (handle_x, y), 10)
    font = pygame.font.Font(None, 24)
    label_surface = font.render(f"{label}: {current_value}", True, colors['DARK_GREY'])
    screen.blit(label_surface, (x - 30, y - 30))


def run_simulation():
    """Main simulation loop for Pygame interaction with the fuzzy irrigation system."""
    screen, clock, colors = initialize_pygame()
    simulation = setup_fuzzy_system()

    slider_positions = {'soil_moisture': 50, 'rain_intensity': 10, 'temperature': 20}
    slider_min_max = {'soil_moisture': (0, 100), 'rain_intensity': (0, 50), 'temperature': (-10, 40)}
    slider_x_pos = {'soil_moisture': 50, 'rain_intensity': 250, 'temperature': 420}
    slider_y_pos = 550

    plant_img = pygame.image.load("resources/plant.png")
    pump_img = pygame.image.load("resources/pump.png")
    plant_img = pygame.transform.scale(plant_img, (300, 300))
    pump_img = pygame.transform.scale(pump_img, (220, 220))

    running = True
    while running:
        screen.fill(colors['WHITE'])
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        screen.blit(plant_img, (400, 200))
        screen.blit(pump_img, (50, 250))

        for label, (min_value, max_value) in slider_min_max.items():
            current_value = slider_positions[label]
            x = slider_x_pos[label]

            if mouse_pressed[0] and abs(mouse_pos[1] - slider_y_pos) < 15 and x < mouse_pos[0] < x + 100:
                new_value = min_value + (mouse_pos[0] - x) / 100 * (max_value - min_value)
                slider_positions[label] = int(np.clip(new_value, min_value, max_value))

            draw_slider(screen, label, x, slider_y_pos, slider_positions[label], min_value, max_value, colors)

        soil_moisture_val = slider_positions['soil_moisture']
        rain_intensity_val = slider_positions['rain_intensity']
        temperature_val = slider_positions['temperature']

        sun_intensity = int(temperature_val * 5)
        pygame.draw.circle(screen, (255, 255, 0), (700, 100), 30 + sun_intensity)

        for _ in range(rain_intensity_val):
            pygame.draw.rect(screen, colors['BLUE'],
                             pygame.Rect(np.random.randint(400, 800), np.random.randint(0, 200), 2, 10))

        simulation.input['soil_moisture'] = soil_moisture_val
        simulation.input['rain_intensity'] = rain_intensity_val
        simulation.input['temperature'] = temperature_val
        simulation.compute()

        start_pos = (260, 320)
        end_pos = (510, 320)
        irrigation_volume_val = simulation.output['irrigation_volume']
        pygame.draw.line(screen, DARK_BLUE, start_pos, end_pos, int(irrigation_volume_val))
        font = pygame.font.Font(None, 36)
        irrigation_text = font.render(f"Irrigation Volume: {irrigation_volume_val:.2f} m^3", True, colors['DARK_BLUE'])
        screen.blit(irrigation_text, (50, 50))
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    run_simulation()
