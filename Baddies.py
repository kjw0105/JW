# Baddies.py
import pygame
import pygwidgets
import random
from Constants import *
from Item import Item

class Baddie(Item):
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 8
    BADDIE_IMAGE = pygame.image.load('images/baddie.png')

    def __init__(self, window):
        size = random.randrange(Baddie.MIN_SIZE, Baddie.MAX_SIZE + 1)
        x = random.randrange(0, WINDOW_WIDTH - size)
        y = 0 - size
        super().__init__(window, x, y, size, Baddie.BADDIE_IMAGE)
        self.speed = random.randrange(Baddie.MIN_SPEED, Baddie.MAX_SPEED + 1)

    def update(self):
        self.y += self.speed
        self.image.setLoc((self.x, self.y))
        return self.y > GAME_HEIGHT
