# SUDOKU SOLVER

This project is a Sudoku Solver that utilizes the backtracking algorithm to solve a randomly generated Sudoku puzzle. The user can choose different difficulty levels and visualize the solving process in real-time using Pygame.

## Result Preview
Below is a GIF demonstrating the Sudoku Solver in action:

![Sudoku Solver in action](img/sudoku_video.gif)

## Features
- Choose difficulty level: Easy, Medium, Expert, or Master.
- Visual representation of the backtracking algorithm solving the Sudoku puzzle.
- Real-time updates showing the solving process and the backtracking steps.

## Prerequisites
- Python 3.6+
- [Pygame](https://www.pygame.org/download.shtml) library

## Installation and Execution
1. Clone this repository:
   ```
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Create and activate a virtual environment:
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Sudoku Solver:
   ```
   python3 Sudoku_Solver.py
   ```

## Usage
- Once the application starts, select the difficulty level by entering the corresponding number (1 for Easy, 2 for Medium, etc.).
- Press the 'B' key to start the backtracking algorithm and watch as the Sudoku is solved in real time.

## License
This project is licensed under the MIT License. (lol)
