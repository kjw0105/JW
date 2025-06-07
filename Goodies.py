# Goodies.py
import pygame
import pygwidgets
import random
from Constants import *
from Item import Item

class Goodie(Item):
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 8
    GOODIE_IMAGE = pygame.image.load('images/goodie.png')
    RIGHT = 'right'
    LEFT = 'left'

    def __init__(self, window):
        size = random.randrange(Goodie.MIN_SIZE, Goodie.MAX_SIZE + 1)
        y = random.randrange(0, GAME_HEIGHT - size)
        direction = random.choice([Goodie.LEFT, Goodie.RIGHT])
        if direction == Goodie.LEFT:
            x = WINDOW_WIDTH
            speed = -random.randrange(Goodie.MIN_SPEED, Goodie.MAX_SPEED + 1)
            self.minLeft = -size
        else:
            x = 0 - size
            speed = random.randrange(Goodie.MIN_SPEED, Goodie.MAX_SPEED + 1)
        super().__init__(window, x, y, size, Goodie.GOODIE_IMAGE)
        self.direction = direction
        self.speed = speed

    def update(self):
        self.x += self.speed
        self.image.setLoc((self.x, self.y))
        if self.direction == Goodie.LEFT:
            return self.x < self.minLeft
        else:
            return self.x > WINDOW_WIDTH
