import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):

    w, rows = 500, 20

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.color = color
        self.dirnx = 1
        self.dirny = 0

    def move(self, dirnx, dirny):
        pass

    def drawCube(self, surface, eyes=False):
        gap = self.w // self.rows
        i, j = self.pos[0], self.pos[1]
        pygame.draw.rect(surface, self.color, (i * gap + 1, j * gap + 1, gap - 2, gap - 2))
        if eyes:
            centre = gap // 2
            radio = 3
            circleMiddle = (i * gap + centre - radio, j*gap + 8)
            circleMiddle2 = (i * gap + gap - radio * 2, j*gap + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radio)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radio)


class snake(object):

    body, turns = [], {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = -1

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def drawSnake(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.drawCube(surface, True)
            else:
                c.drawCube(surface)


def drawGrid(w, rows, surface):
    gap = w // rows
    x, y = 0, 0
    for f in range(rows):
        x, y = x + gap, y + gap
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global width, rows, snack
    surface.fill((10, 10, 0))
    drawGrid(width, rows, surface)
    s.drawSnake(surface)
    snack.drawCube(surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return (x, y)


def message_box(subject, content):
    pass


def main():
    global width, rows, s, snack
    width = 500
    rows = width // 25
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color=(0, 255, 0))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        redrawWindow(win)


main()
