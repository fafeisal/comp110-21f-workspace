import sys
import pygame as py
from vector import Vector
from gm import GameManager
from snake import Snake
from food import Food
import pygame_gui
py.init()

# Window
size = width, height = 900, 600

# RGBA constants
bkgd = 173, 223, 179
color = 100, 50, 20, 10
snake_color = 255, 109, 106

FRAMES = 60


# Makes Screen
screen = py.display.set_mode(size)

# Game clock
clock = py.time.Clock()

# Keeps game loop running
playing = True

# Handles GUI
manager = pygame_gui.UIManager((width, height))

snake_position: Vector = Vector(50, 200)

george: Snake = Snake(snake_position, snake_color, 4.0)

food_color = 0, 1, 1
first: Food = Food(Vector(100, 100), food_color)

snake_list: list[Snake] = []

# UI Elements for GUI
snake_total = pygame_gui.elements.UILabel(relative_rect=py.Rect((420, 40), (200, 50)),
                text='Snake: ' + str(len(snake_list)),
                manager=manager)

# Game Loop
while playing:
    # Games internal clock, sets number of frames run per second
    clock.tick(FRAMES)

    pos = py.mouse.get_pos()
    # Tracks player interaction
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
        # Places fighter if game manager agrees
        if event.type == py.MOUSEBUTTONUP:
            snake_list.append(Snake(Vector(pos[0], pos[1]), snake_color, 5.0))

    screen.fill(bkgd)
    
    py.draw.circle(screen, first.color, (first.position.x, first.position.y), 5)
    # for snake in snake_list:
    py.draw.circle(screen, george.color, (george.position.x, george.position.y), 20)
    george.move_snake(Vector(pos[0] + 1, pos[1] + 1))

    george.move_snake(Vector(pos[0] + 1, pos[1] + 1))
    # GUI Updates
    snake_total.set_text("Points: " + str(len(snake_list)))
    manager.process_events(event)
    manager.update(20)
    manager.draw_ui(screen)

    # Flips all the updates from the loop onto screen
    py.display.update()