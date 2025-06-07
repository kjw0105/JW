# ItemMgr.py
import random

class ItemMgr:
    def __init__(self, window, ItemClass, add_rate=8, *args, **kwargs):
        self.window = window
        self.ItemClass = ItemClass  # Baddie, Goodie 등 클래스를 받음
        self.itemList = []
        self.add_rate = add_rate
        self.nFramesTilNextItem = add_rate
        self.args = args
        self.kwargs = kwargs

    def reset(self):
        self.itemList = []
        self.nFramesTilNextItem = self.add_rate

    def update(self, *collision_args):
        nRemoved = 0
        itemListCopy = self.itemList.copy()
        for item in itemListCopy:
            deleteMe = item.update()
            if deleteMe:
                self.itemList.remove(item)
                nRemoved += 1
            elif collision_args:
                # collision_args는 플레이어 rect 등
                if hasattr(item, 'collide') and item.collide(*collision_args):
                    self.itemList.remove(item)
                    nRemoved += 1

        self.nFramesTilNextItem -= 1
        if self.nFramesTilNextItem <= 0:
            newItem = self.ItemClass(self.window, *self.args, **self.kwargs)
            self.itemList.append(newItem)
            self.nFramesTilNextItem = self.add_rate  # 혹은 Goodie는 랜덤 범위

        return nRemoved

    def draw(self):
        for item in self.itemList:
            item.draw()

  # ItemMgr.py 내부에 추가
    def hasPlayerHitBaddie(self, playerRect):
        return self.hasPlayerHitItem(playerRect)

    def hasPlayerHitGoodie(self, playerRect):
        return self.hasPlayerHitItem(playerRect)

    def hasPlayerHitItem(self, playerRect):
        for item in self.itemList:
            if item.collide(playerRect):
                return True
        return False
