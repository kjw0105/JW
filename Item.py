# Item.py
import pygame
import random
import pygwidgets
from Constants import *

class Item():
    def __init__(self, window, windowWidth, windowHeight, item_type, max_speed=None):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.item_type = item_type  # 'baddie', 'score', 'health', 'shield'

        if self.item_type == 'baddie':
            size = random.randrange(BADDIE_MIN_SIZE, BADDIE_MAX_SIZE + 1)
            self.x = random.randrange(0, self.windowWidth - size)
            self.y = 0 - size
            image = pygame.image.load('images/baddie.png')
            self.image = pygwidgets.Image(self.window, (self.x, self.y), image)
            percent = (size * 100) / BADDIE_MAX_SIZE
            self.image.scale(percent, False)
            self.speed = random.randrange(BADDIE_MIN_SPEED, max_speed + 1)
        else:
            if self.item_type == 'score':
                goodieImage = pygame.image.load('images/goodie.png')
            elif self.item_type == 'health':
                goodieImage = pygame.image.load('images/health.png')
            elif self.item_type == 'shield':
                goodieImage = pygame.image.load('images/shield.png')
            else:
                raise ValueError("알 수 없는 아이템 타입")

            goodieSize = random.randint(GOODIE_MIN_SIZE, GOODIE_MAX_SIZE)
            self.goodieImage = pygame.transform.scale(goodieImage, (goodieSize, goodieSize))
            self.goodieRect = self.goodieImage.get_rect()
            self.goodieRect.left = random.randint(0, self.windowWidth - self.goodieRect.width)
            self.goodieRect.top = 0 - self.goodieRect.height
            self.xVel = 0
            self.yVel = random.randint(BADDIE_MIN_SPEED, BADDIE_MAX_SPEED)

    def update(self):
        if self.item_type == 'baddie':
            self.y += self.speed
            self.image.setLoc((self.x, self.y))
            return self.y > GAME_HEIGHT
        else:
            self.goodieRect.left += self.xVel
            self.goodieRect.top += self.yVel
            return self.goodieRect.top > self.windowHeight

    def draw(self):
        if self.item_type == 'baddie':
            self.image.draw()
        else:
            self.window.blit(self.goodieImage, self.goodieRect)

    def collide(self, playerRect):
        if self.item_type == 'baddie':
            return self.image.overlaps(playerRect)
        else:
            return playerRect.colliderect(self.goodieRect)

    def getType(self):
        return self.item_type

    def getRect(self):
        if self.item_type == 'baddie':
            return self.image.getRect()
        else:
            return self.goodieRect
