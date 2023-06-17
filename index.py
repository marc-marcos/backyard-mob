import pygame 
import random
import time
from logic import update_cells, check_winnage

pygame.init()

HEIGHT = 800
WIDTH = 800

ROW_COUNT = 20 

pygame.display.set_caption("Backyard Mob")
window_surface = pygame.display.set_mode((HEIGHT, WIDTH))

background = pygame.Surface((HEIGHT, WIDTH))
background.fill(pygame.Color("#313131"))

is_running = True

cell_matrix = [[random.randint(0, 2) for i in range(ROW_COUNT)] for j in range(ROW_COUNT)]
print(cell_matrix)

iteraciones = 0

while is_running:
    cell_matrix = update_cells(cell_matrix)
    winnage = check_winnage(cell_matrix)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Drawing the background
    for i in range(ROW_COUNT):
        for j in range(ROW_COUNT):
            pygame.draw.rect(
                window_surface,
                pygame.Color("#FFFFFF"),
                pygame.Rect(i * (HEIGHT/ROW_COUNT), j * (WIDTH/ROW_COUNT), (HEIGHT/ROW_COUNT), (WIDTH/ROW_COUNT)),
                1
            )

    # Drawing the cells
    for i in range(ROW_COUNT):
        for j in range(ROW_COUNT):
            if cell_matrix[i][j] == 1:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#2596be"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT)+1, j * (WIDTH/ROW_COUNT)+1, (HEIGHT/ROW_COUNT)-1, (WIDTH/ROW_COUNT)-1),
                    0
                )
            
            if cell_matrix[i][j] == 0:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#313131"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT)+1, j * (WIDTH/ROW_COUNT)+1, (HEIGHT/ROW_COUNT)-1, (WIDTH/ROW_COUNT)-1),
                    0
                )
            
            if cell_matrix[i][j] == 2:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#ff5733"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT)+1, j * (WIDTH/ROW_COUNT)+1, (HEIGHT/ROW_COUNT)-1, (WIDTH/ROW_COUNT)-1),
                    0
                )

    iteraciones += 1

    pygame.display.update()
    
    if winnage == 1:
        print(f"Team A wins!, {iteraciones} iterations")
        time.sleep(5)
        is_running = False
    
    elif winnage == 2:
        print(f"Team B wins!, {iteraciones} iterations")
        time.sleep(5)
        is_running = False

    # Updating the cells
    time.sleep(0.1)
