# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

## Setup ##
pg.init()
screen = pg.display.set_mode((300,400))
pg.display.set_caption("Pac-Man (clone)")

x = 300/2 
y = 400/2 

pacman_images = []
for i in range(6):
    img = pg.image.load(f"images/pacman_{i}.png")
    pacman_images.append(img)

direction = None
running = True
tick = 0
while running:


    # Event loop
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                direction = "left"
            elif event.key == pg.K_RIGHT:
                direction = "right"
            elif event.key == pg.K_UP:
                direction = "up"
            elif event.key == pg.K_DOWN:
                direction = "down"
            elif event.key == pg.K_ESCAPE:
                running = False

    # Move
    if direction == "left":
        x = x - 5
    elif direction == "right":
        x = x + 5
    elif direction == "up":
        y = y - 5
    elif direction == "down":
        y = y + 5


    # Draw
    screen.fill((0,0,0))

    r = tick%6
    screen.blit(pacman_images[r], (x, y))
            

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.05)
