# Gesture-Based Music Control

## Introduction
This project implements a gesture recognition system using Python, OpenCV, and MediaPipe to control a music player. The system detects hand gestures via a webcam and translates them into media control commands, such as:
- **Point Right** → Next Track
- **Point Left** → Previous Track
- **Point Up** → Increase Volume
- **Point Down** → Decrease Volume

The processing is done on a color video feed, but the preview display is shown in black and white for better contrast.

## Requirements
- **Operating System:** Linux (required for full functionality)
- **Python Libraries:**
  - OpenCV
  - MediaPipe
  - NumPy
  - PyAutoGUI
  - xdotool (installed on the system for key simulation)

## How It Works
1. Captures video from the webcam.
2. Detects hand landmarks using MediaPipe.
3. Analyzes the direction in which the index finger is pointing.
4. Triggers the corresponding music control action using `xdotool`.
5. Displays a black-and-white preview while processing the original color feed.

## Running the Program
Make sure you have all dependencies (also located in `../requirements.txt`) installed and run:
```bash
python3 gesture_music_control.py
```
Press 'q' to exit the program.

## Notes
- The script uses `xdotool`, which is specific to Linux environments, to simulate media key presses.
- If `xdotool` is not installed, install it using:
```bash
sudo apt install xdotool
```
- The system resets gesture recognition when the index finger is not extended to prevent repeated actions.

## Demo
_mp4 file with audio is located under `./media/computer_vision_gestures_demo.mp4`_

![](./media/computer_vision_gestures_demo.gif)
