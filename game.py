# Pac-Man clone made for learning/teaching
import time
import random
import pygame as pg

## Screen setup ##
pg.init()
screen = pg.display.set_mode((600,800))
pg.display.set_caption("Pac-Man (clone)")

##Sound

pg.mixer.pre_init(44100,32,2,1024)
pg.mixer.init()
pg.mixer.music.load("pacman_banging.wav")
pg.mixer.music.play()

## Load images ##
pacman_images = []
for i in range(6):
    img = pg.image.load(f"images/pacman_{i}.png")
    img = pg.transform.scale(img, (32,32))
    pacman_images.append(img)

ghost_images = []

for m in range(2):
    img = pg.image.load(f"images/GHOSTY_{m}.png")
    img = pg.transform.scale(img, (32,32))
    ghost_images.append(img)


## Level ##
level = []
with open('level.txt', 'r') as level_file:
    for r, line in enumerate(level_file):
        row = []
        for c, char in enumerate(line):
            if char == "#":
                row.append("#")
            elif char == "p":
                y = r*32
                x = c*32
                row.append(" ")
            elif char == "g":
                x1 = r*32
                y1 = c*32
                row.append(" ")
            else:
                row.append(" ")

        level.append(row)

num_rows = len(level)
num_cols = len(level[0])



## Game Loop ##
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
            if event.key == pg.K_a:
                direction = "left"
            elif event.key == pg.K_d:
                direction = "right"
            elif event.key == pg.K_w:
                direction = "up"
            elif event.key == pg.K_s:
                direction = "down"
            elif event.key == pg.K_SPACE:
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

    ghostmove = (random.randint(1,10))

    if ghostmove == (1 or 2):
        x1 = x1 - 5
    elif ghostmove == (3 or 4):
        x1 = x1 + 5
    elif ghostmove == (5 or 6):
        y1 = y1 - 5
    elif ghostmove == (7 or 8):
        y1 = y1 + 5


    # Draw level #
    screen.fill((0,0,0))
    for r, row in enumerate(level):
        for c, tile in enumerate(row):
            left = c*32
            top = r*32
            if tile == "#":
                pg.draw.rect(screen, (20,20,220), pg.Rect(left+1, top+1, 30,30), 1)



    # Draw pacman#
    r = int((tick/2)%6)
    if direction == "left":
        screen.blit(pacman_images[r], (x, y))
    elif direction == "right":
        screen.blit(pg.transform.rotate(pacman_images[r],180), (x, y))
    elif direction == "up":
        screen.blit(pg.transform.rotate(pacman_images[r],-90), (x, y))
    elif direction == "down":
        screen.blit(pg.transform.rotate(pacman_images[r],90), (x, y))
    else:
        screen.blit(pacman_images[0], (x, y))

    # Draw Ghost

    g = int((tick/2)%2)
    if direction == "left":
        screen.blit(ghost_images[g], (x1, y1))
    elif direction == "right":
        screen.blit(pg.transform.rotate(ghost_images[g],180), (x1, y1))
    elif direction == "up":
        screen.blit(pg.transform.rotate(ghost_images[g],-90), (x1, y1))
    elif direction == "down":
        screen.blit(pg.transform.rotate(ghost_images[g],90), (x1, y1))
    else:
        screen.blit(ghost_images[0], (x1, y1))
            

    # Update screen
    pg.display.flip()

    # Framerate (limit by doing nothing)
    tick += 1
    time.sleep(0.05)
