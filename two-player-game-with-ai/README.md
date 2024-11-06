# Chomp Game

This project is a Python implementation of the classic two-player game **Chomp** using the `easyAI` library. The game simulates players taking turns to "chomp" sections of a grid, with the goal of not being forced to eat the last square (top-left corner).

## How to Play

1. **Game Setup:** The game is played on a grid (default size is 5x5). Players take turns picking a square. All squares to the right and below the chosen square (including the chosen one) are "chomped" and no longer available.
2. **Objective:** The player who is forced to chomp the top-left corner (square "A1") loses the game.

## Running the Game

It is recommended to run the code inside a [Python virtual environment](https://docs.python.org/3/library/venv.html) (`venv`) to isolate the dependencies.

### Steps:

1. Install the dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the game
   ```bash
    python chomp.py
    ```
    You can modify the board size by changing the `board_size` argument in the Chomp class initialization in the code.
### Dependencies
The required libraries for this game are listed in requirements.txt, which includes:

- easyAI: A Python library to implement two-player AI-based games.
- numpy: For handling the grid-based board efficiently.

### Example
```bash
python chomp.py

  1 2 3 4 5
A O O O O O
B O O O O O
C O O O O O
D O O O O O
E O O O O O

Player 1, what do you play? D3

Move #1: Player 1 plays D3

  1 2 3 4 5
A O O O O O
B O O O O O
C O O O O O
D O O X X X
E O O X X X
```
### Screenshots
![image](https://github.com/user-attachments/assets/aa2579cb-f963-410a-b668-e713742ebbf6)