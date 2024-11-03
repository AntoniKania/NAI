import pygame.freetype
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

soil_moisture_range = np.arange(0, 101, 1)
rain_intensity_range = np.arange(0, 51, 1)
temperature_range = np.arange(-10, 41, 1)
irrigation_volume_range = np.arange(0, 51, 1)

soil_moisture = ctrl.Antecedent(soil_moisture_range, 'soil_moisture')
rain_intensity = ctrl.Antecedent(rain_intensity_range, 'rain_intensity')
temperature = ctrl.Antecedent(temperature_range, 'temperature')
irrigation_volume = ctrl.Consequent(irrigation_volume_range, 'irrigation_volume')

soil_moisture['dry'] = fuzz.trapmf(soil_moisture_range, [0, 0, 20, 40])
soil_moisture['optimal'] = fuzz.trapmf(soil_moisture_range, [30, 50, 50, 70])
soil_moisture['wet'] = fuzz.trapmf(soil_moisture_range, [60, 80, 100, 100])

rain_intensity['none'] = fuzz.trapmf(rain_intensity_range, [0, 0, 5, 10])
rain_intensity['light'] = fuzz.trimf(rain_intensity_range, [5, 15, 25])
rain_intensity['moderate'] = fuzz.trimf(rain_intensity_range, [20, 30, 40])
rain_intensity['heavy'] = fuzz.trapmf(rain_intensity_range, [35, 45, 50, 50])

temperature['cold'] = fuzz.trapmf(temperature_range, [-10, -10, 5, 15])
temperature['moderate'] = fuzz.trapmf(temperature_range, [10, 20, 25, 30])
temperature['hot'] = fuzz.trapmf(temperature_range, [25, 30, 40, 40])

irrigation_volume['none'] = fuzz.trimf(irrigation_volume_range, [0, 0, 5])
irrigation_volume['small'] = fuzz.trimf(irrigation_volume_range, [5, 10, 20])
irrigation_volume['medium'] = fuzz.trimf(irrigation_volume_range, [15, 25, 35])
irrigation_volume['large'] = fuzz.trimf(irrigation_volume_range, [30, 40, 50])

rule1 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['none'] & temperature['hot'], irrigation_volume['large'])
rule2 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['light'] & temperature['moderate'], irrigation_volume['medium'])
rule12 = ctrl.Rule(soil_moisture['optimal'] & rain_intensity['heavy'] & temperature['moderate'], irrigation_volume['none'])
rule3 = ctrl.Rule(soil_moisture['optimal'] & rain_intensity['moderate'], irrigation_volume['small'])
rule8 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['moderate'], irrigation_volume['medium'])
rule10 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['heavy'], irrigation_volume['none'])
rule11 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['heavy'] & temperature['moderate'], irrigation_volume['none'])
rule9 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['moderate'] & temperature['hot'], irrigation_volume['medium'])
rule4 = ctrl.Rule(soil_moisture['wet'] | rain_intensity['heavy'], irrigation_volume['none'])
rule5 = ctrl.Rule(soil_moisture['optimal'] & temperature['cold'], irrigation_volume['none'])
rule6 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['none'] & temperature['cold'], irrigation_volume['medium'])
rule7 = ctrl.Rule(soil_moisture['dry'] & rain_intensity['none'] & temperature['moderate'], irrigation_volume['medium'])

general_rule = ctrl.Rule(soil_moisture['dry'], irrigation_volume['medium'])
general_rule_2 = ctrl.Rule(soil_moisture['wet'], irrigation_volume['none'])
general_rule_3 = ctrl.Rule(soil_moisture['optimal'], irrigation_volume['small'])
general_rule_4 = ctrl.Rule(rain_intensity['heavy'], irrigation_volume['none'])
general_rule_5 = ctrl.Rule(rain_intensity['moderate'], irrigation_volume['small'])

irrigation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule12, rule11,
                                      general_rule, general_rule_2, general_rule_3, general_rule_4, general_rule_5])
irrigation_sim = ctrl.ControlSystemSimulation(irrigation_ctrl)

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Automatic Irrigation System")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
DARK_BLUE = (0, 102, 204)
LIGHT_GRAY = (200, 200, 200)

font = pygame.freetype.SysFont(None, 24)

plant_img = pygame.image.load("resources/plant.png")
pump_img = pygame.image.load("resources/pump.png")
plant_img = pygame.transform.scale(plant_img, (300, 300))
pump_img = pygame.transform.scale(pump_img, (220, 220))

input_boxes = {
    "soil_moisture": {"value": "", "rect": pygame.Rect(50, 500, 100, 32)},
    "rain_intensity": {"value": "", "rect": pygame.Rect(280, 500, 100, 32)},
    "temperature": {"value": "", "rect": pygame.Rect(570, 500, 100, 32)}
}

irrigation_volume_val = 0

running = True
active_input = None
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    screen.blit(plant_img, (400, 200))
    screen.blit(pump_img, (50, 250))

    for name, box in input_boxes.items():
        pygame.draw.rect(screen, LIGHT_GRAY, box["rect"])
        font.render_to(screen, (box["rect"].x + 5, box["rect"].y + 5), box["value"], BLACK)

    font.render_to(screen, (50, 470), "Soil Moisture (%)", BLACK)
    font.render_to(screen, (280, 470), "Rain Intensity (mm/hr)", BLACK)
    font.render_to(screen, (570, 470), "Temperature (°C)", BLACK)

    font.render_to(screen, (50, 50), f"Irrigation Volume: {irrigation_volume_val:.2f} m³", BLACK)

    sun_intensity = int(float(input_boxes["temperature"]["value"] or 0) * 5)
    pygame.draw.circle(screen, (255, 255, 0), (700, 100), 30 + sun_intensity)

    rain_drops = int(float(input_boxes["rain_intensity"]["value"] or 0) * 2)
    for _ in range(rain_drops):
        pygame.draw.rect(screen, BLUE, pygame.Rect(np.random.randint(400, 800), np.random.randint(0, 200), 2, 10))

    start_pos = (250, 300)
    max_length = 300
    line_length = int((irrigation_volume_val / 50) * max_length)
    end_pos = (550, 300)

    pygame.draw.line(screen, DARK_BLUE, start_pos, end_pos, int(irrigation_volume_val))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for name, box in input_boxes.items():
                if box["rect"].collidepoint(event.pos):
                    active_input = name
                    break

        elif event.type == pygame.KEYDOWN:
            if active_input and event.key == pygame.K_RETURN:
                try:
                    soil_moisture = float(input_boxes["soil_moisture"]["value"])
                    rain_intensity = float(input_boxes["rain_intensity"]["value"])
                    temperature = float(input_boxes["temperature"]["value"])

                    irrigation_sim.input['soil_moisture'] = soil_moisture
                    irrigation_sim.input['rain_intensity'] = rain_intensity
                    irrigation_sim.input['temperature'] = temperature
                    irrigation_sim.compute()

                    irrigation_volume_val = irrigation_sim.output['irrigation_volume']
                except ValueError:
                    print("Invalid input")
                active_input = None
            elif active_input:
                if event.key == pygame.K_BACKSPACE:
                    input_boxes[active_input]["value"] = input_boxes[active_input]["value"][:-1]
                else:
                    input_boxes[active_input]["value"] += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
