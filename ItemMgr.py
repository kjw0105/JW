# ItemMgr.py
import random
from Constants import *
from Item import Item

class ItemMgr():
    def __init__(self, window):
        self.window = window
        self.windowWidth = window.get_width()
        self.windowHeight = window.get_height()
        self.itemsList = []
        self.nFramesTilNextBaddie = BADDIE_ADD_NEW_FREQ
        self.current_max_speed = BADDIE_MAX_SPEED
        self.goodie_rate_hi = GOODIE_ADD_NEW_FREQ
        self.goodie_rate_low = GOODIE_ADD_NEW_FREQ * GOODIE_ADD_NEW_RATE

    def reset(self):
        self.itemsList = []
        self.nFramesTilNextBaddie = BADDIE_ADD_NEW_FREQ
        self.current_max_speed = BADDIE_MAX_SPEED
        self.goodie_rate_hi = GOODIE_ADD_NEW_FREQ
        self.goodie_rate_low = GOODIE_ADD_NEW_FREQ * GOODIE_ADD_NEW_RATE

    def update(self, playerRect, level_factor):
        # Baddie 생성
        self.current_max_speed = BADDIE_MAX_SPEED + int(level_factor * 5)
        if self.current_max_speed > 20: self.current_max_speed = 20
        self.nFramesTilNextBaddie -= 1
        if self.nFramesTilNextBaddie == 0:
            oBaddie = Item(self.window, self.windowWidth, self.windowHeight, 'baddie', self.current_max_speed)
            self.itemsList.append(oBaddie)
            self.nFramesTilNextBaddie = BADDIE_ADD_NEW_FREQ - int(level_factor * 2)
            if self.nFramesTilNextBaddie < 1: self.nFramesTilNextBaddie = 1

        # Goodie 생성
        if random.randrange(random.randint(int(self.goodie_rate_low), int(self.goodie_rate_hi))) == 0:
            gtype = random.choice(['score', 'health', 'shield'])
            oGoodie = Item(self.window, self.windowWidth, self.windowHeight, gtype)
            self.itemsList.append(oGoodie)

        # 업데이트 및 충돌 처리
        hitTypes = []
        for item in self.itemsList[:]:
            offscreen = item.update()
            if item.getType() == 'baddie':
                if item.collide(playerRect):
                    self.itemsList.remove(item)
                    hitTypes.append(('baddie', item))
                elif offscreen:
                    self.itemsList.remove(item)
            else:
                if item.collide(playerRect):
                    hitTypes.append((item.getType(), item))
                    self.itemsList.remove(item)
                elif offscreen:
                    self.itemsList.remove(item)
        return hitTypes

    def draw(self):
        for item in self.itemsList:
            item.draw()
