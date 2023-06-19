import pygame 
from pygame.locals import *
import random
import time
from logic import update_cells, check_winnage

from tkinter import *
from tkinter import messagebox

messagebox.showinfo("Tutorial", "In the next screen click left button of your mouse to generate a random pattern and space to start the game.")

pygame.init()

HEIGHT = 900
WIDTH = 900

ROW_COUNT = 100 

pygame.display.set_caption("Backyard Mob")
window_surface = pygame.display.set_mode((HEIGHT, WIDTH))

background = pygame.Surface((HEIGHT, WIDTH))
background.fill(pygame.Color("#313131"))


cell_matrix = [[0 for i in range(ROW_COUNT)] for j in range(ROW_COUNT)]


is_running_creation = True
while is_running_creation:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                is_running_creation = False
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                cell_matrix = [[random.randint(0,2) for i in range(ROW_COUNT)] for j in range(ROW_COUNT)]

    # Drawing the cells
    for i in range(ROW_COUNT):
        for j in range(ROW_COUNT):
            if cell_matrix[i][j] == 1:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#2596be"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT), j * (WIDTH/ROW_COUNT), (HEIGHT/ROW_COUNT), (WIDTH/ROW_COUNT)),
                    0
                )
            
            if cell_matrix[i][j] == 0:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#313131"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT), j * (WIDTH/ROW_COUNT), (HEIGHT/ROW_COUNT), (WIDTH/ROW_COUNT)),
                    0
                )
            
            if cell_matrix[i][j] == 2:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#ff5733"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT), j * (WIDTH/ROW_COUNT), (HEIGHT/ROW_COUNT), (WIDTH/ROW_COUNT)),
                    0
                )

    pygame.display.update()
    time.sleep(0.1)

iteraciones = 0

is_running = True

while is_running:
    cell_matrix = update_cells(cell_matrix)
    winnage = check_winnage(cell_matrix)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Drawing the cells
    for i in range(ROW_COUNT):
        for j in range(ROW_COUNT):
            if cell_matrix[i][j] == 1:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#2596be"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT), j * (WIDTH/ROW_COUNT), (HEIGHT/ROW_COUNT), (WIDTH/ROW_COUNT)),
                    0
                )
            
            if cell_matrix[i][j] == 0:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#313131"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT)+1, j * (WIDTH/ROW_COUNT), (HEIGHT/ROW_COUNT), (WIDTH/ROW_COUNT)),
                    0
                )
            
            if cell_matrix[i][j] == 2:
                pygame.draw.rect(
                    window_surface,
                    pygame.Color("#ff5733"),
                    pygame.Rect(i * (HEIGHT/ROW_COUNT), j * (WIDTH/ROW_COUNT), (HEIGHT/ROW_COUNT), (WIDTH/ROW_COUNT)),
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
    pygame.time.delay(1)
