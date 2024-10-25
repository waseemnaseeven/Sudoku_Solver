import pygame
import random
import time
import os
import sys
import math

# Sudoku rule : 1 chiffre ne peut apparaitre qu'une fois par ligne, colonne et bloc de 3x3

# Backtracking : Essayer un chiffre de 1 a 9, si le chiffre choisi est valide, next, sinon on revient a la decision precedente

def get_difficulty() -> int:
    print("You can choose the level of difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Expert")
    print("4. Master")

    try:
        option = int(input("Enter the number of your choice: "))
    except:
        print("Invalid input. Please enter a number between 1 and 4.")
        return None

    return option

def init_grid(option) -> list:
    # Return a 3x3x3 
    # grid_3x3x3 = [[[random.randint(1,9) for _ in range(3)] for _ in range(3)] for _ in range(3)]
     # Or return 9x9 
    # grid_9x9 = [[random.randint(1,9) for _ in range(9)] for _ in range(9)]
    
    grid_9x9 = [[0 for _ in range(9)] for _ in range(9)]
    filled_cells = 0
    if option == 1:
        filled_cells = random.randint(35, 40)
    elif option == 2:
        filled_cells = random.randint(30, 34)
    elif option == 3:
        filled_cells = random.randint(25, 29)
    elif option == 4:
        filled_cells = random.randint(17, 24)
    
    cells = random.sample(range(81), filled_cells) # Va choisir aleatoirement les cellules de 0 a 80
    for cell in cells:
        row, col = divmod(cell, 9) # renvoie un tuple contenant le quotient et le reste de la division de cell par 9.
        digit = random.randint(1, 9)
        while not is_valid_move(grid_9x9, row, col, digit):
            digit = random.randint(1, 9)    
        grid_9x9[row][col] = digit
    return grid_9x9

def draw_grid(screen, screen_size, margin, cell_size):
    for i in range(10):
        line_thickness = 1
        color = (192, 192, 192)
        if i % 3 == 0:
            line_thickness = 3
            color = (0, 0, 0)
        # Tracage des lignes a la vertical
        pygame.draw.line(screen, color, (margin // 2 + i * cell_size, margin), (margin // 2 + i * cell_size, screen_size - margin // 2), line_thickness)
        # Tracage des lignes a l'horizontal
        pygame.draw.line(screen, color, (margin // 2, margin + i * cell_size), (screen_size - margin , margin + i * cell_size), line_thickness)


def draw_informations(screen, option, backtracking_time):
    font = pygame.font.Font(None, 36)
    difficulty_levels = {1: "Easy", 2: "Medium", 3: "Expert", 4: "Master"}
    difficulty_text = font.render(f"Difficulty: {difficulty_levels.get(option, 'Chosen Level')}", True, (0, 0, 0))
    screen.blit(difficulty_text, (10, 10))
    backtracking_text = font.render(f"Backtracking Time: {backtracking_time:.2f}ms", True, (0, 0, 0))
    screen.blit(backtracking_text, (10, 40))


def draw_numbers(screen, grid, margin, cell_size):
    font = pygame.font.Font(None, 40)
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                value = str(grid[row][col])
                text = font.render(value, True, (0, 0, 0))
                text_rect = text.get_rect(center=(margin // 2 + col * cell_size + cell_size // 2, margin + row * cell_size + cell_size // 2))
                screen.blit(text, text_rect)

def draw_functions(screen, screen_size, margin, cell_size, grid, option, backtracking_time):
    screen.fill((255, 255, 255)) # Remplir l'écran avec un fond blanc avant de dessiner
    draw_grid(screen, screen_size, margin, cell_size) # Affichage de la grille de sudoku
    draw_numbers(screen, grid, margin, cell_size) # Affichage des chiffres de 1 a 9
    draw_informations(screen, option, backtracking_time) # Affichage de la difficulte 

def is_valid_move(grid, row, col, digit) -> bool:
    for i in range(9):
        # Verifier la premiere ligne si le digit est deja present
        if grid[row][i] == digit or grid[i][col] == digit:
            return False
    # Verifier si le digit existe sur le coin superieur gauche de chaque 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    # Parcourir 
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == digit:
                return False
    return True


def backtracking_algorithm(grid, screen, margin, cell_size, option, start_time) -> bool:
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1, 10):
                    print(f"Digit : {digit}")
                    if is_valid_move(grid, row, col, digit):
                        grid[row][col] = digit
                        print(f"Trying digit {digit} at position ({row}, {col})")  # Ajout de debug

                        backtracking_time = (time.time() - start_time) * 1000
                        draw_functions(screen, grid_size * cell_size, margin, cell_size, grid, option, backtracking_time)
                        pygame.display.flip()
                        pygame.time.delay(50)

                        if backtracking_algorithm(grid, screen, margin, cell_size, option, start_time):
                            return True
                        
                        grid[row][col] = 0
                        print(f"Backtracking at position ({row}, {col}) now is {grid[row][col]}")  # Ajout de debug
                        backtracking_time = (time.time() - start_time) * 1000

                        draw_functions(screen, grid_size * cell_size, margin, cell_size, grid, option, backtracking_time)
                        pygame.display.flip()
                        pygame.time.delay(50)
                return False
    return True


def is_grid_valid(grid):
    for i in range(9):
        for j in range(9):
            digit = grid[i][j]
            if digit!= 0:
                grid[i][j] = 0 # Changement temporaire de la valeur
                if not is_valid_move(grid, i, j, digit):
                    return False
                grid[i][j] = digit # On remet la valeur
    return True

def main(grid_size, cell_size):
    pygame.init()
    margin = 80 # offset
    screen_size = grid_size * cell_size 
    screen = pygame.display.set_mode((screen_size - margin // 2, screen_size)) # Fenetre de dimension (largeur, hauteur)
    pygame.display.set_caption("Sudoku Solver") # Titre de la fenetre
    option = get_difficulty()
    if not option:
        return None
    grid = init_grid(option)
    if not is_grid_valid(grid):
        print("The initial grid is not valid and cannot be solved.")
        pygame.quit()
        return main(grid_size, cell_size)
    clock = pygame.time.Clock()
    run = True
    while run:
        start_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                backtracking_algorithm(grid, screen, margin, cell_size, option, start_time)
                print("OVER")
        draw_functions(screen, screen_size, margin, cell_size, grid, option, start_time)
        pygame.display.flip()
        pygame.time.delay(50)
        clock.tick(60)

        backtracking_algorithm(grid, screen, margin, cell_size, option, start_time)
    pygame.quit()

if __name__ == '__main__':
    grid_size = 11
    cell_size = 60
    main(grid_size, cell_size)