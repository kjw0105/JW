# Item.py
import pygwidgets

class Item:
    def __init__(self, window, x, y, size, image):
        self.window = window
        self.x = x
        self.y = y
        self.size = size
        self.image = pygwidgets.Image(self.window, (self.x, self.y), image)
        percent = int((size * 100) / 40)  # MAX_SIZE 가정
        self.image.scale(percent, False)

    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        return self.image.overlaps(playerRect)
