import cv2
import mediapipe as mp
import numpy as np
import os


def control_music(action):
    """
    Controls the music player using system commands.

    Args:
        action (str): The action to perform ("next", "prev", "volume_up", "volume_down").
    """
    commands = {
        "next": "xdotool key XF86AudioNext",
        "prev": "xdotool key XF86AudioPrev",
        "volume_up": "xdotool key XF86AudioRaiseVolume",
        "volume_down": "xdotool key XF86AudioLowerVolume",
    }
    if action in commands:
        os.system(commands[action])


def process_hand_landmarks(hand_landmarks, frame):
    """
    Processes hand landmarks to determine the gesture direction.

    Args:
        hand_landmarks: MediaPipe hand landmarks.
        frame (numpy.ndarray): The current video frame.

    Returns:
        str or None: The detected gesture ("next", "prev", "volume_up", "volume_down") or None.
    """
    h, w, _ = frame.shape
    index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_MCP]

    index_tip_x, index_tip_y = int(index_tip.x * w), int(index_tip.y * h)
    index_mcp_x, index_mcp_y = int(index_mcp.x * w), int(index_mcp.y * h)

    delta_x = index_tip_x - index_mcp_x
    delta_y = index_tip_y - index_mcp_y

    mcp_distance = np.linalg.norm(
        np.array([index_tip_x, index_tip_y]) - np.array([index_mcp_x, index_mcp_y])
    )

    if mcp_distance < 80:
        return None

    if abs(delta_x) > abs(delta_y):
        return "next" if delta_x > 0 else "prev"
    else:
        return "volume_up" if delta_y < 0 else "volume_down"


def apply_black_white_filter(frame):
    """
    Converts a frame to a high-contrast black-and-white image.

    Args:
        frame (numpy.ndarray): The original frame.

    Returns:
        numpy.ndarray: The black-and-white filtered frame.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)


def main():
    """
    Main function to capture video, detect hand gestures, and control the music player.
    """
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    last_gesture = None

    with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb_frame)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    new_gesture = process_hand_landmarks(hand_landmarks, frame)

                    if new_gesture and new_gesture != last_gesture:
                        print(f"Gesture Detected: {new_gesture}")
                        control_music(new_gesture)
                        last_gesture = new_gesture
            else:
                last_gesture = None

            frame_bw = apply_black_white_filter(frame)
            cv2.imshow("Gesture Control", frame_bw)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
