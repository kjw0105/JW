import pygame
import pygwidgets
import pyghelpers 
from Constants import * 

class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.title = pygwidgets.DisplayText(self.window, (0, 100), "Dodger!",
                                             fontSize=100, textColor=WHITE,
                                             width=WINDOW_WIDTH, justified='center')

        self.instructions1 = pygwidgets.DisplayText(self.window, (120, 250),
                                                    "This is you. Drag the icon around by\nmoving the mouse.",
                                                    fontSize=36, textColor=WHITE)
        self.playerImage = pygwidgets.Image(self.window, (40, 250), pygame.image.load('images/player.png'))

        self.instructions2 = pygwidgets.DisplayText(self.window, (120, 320),
                                                    "Dodge the Baddies. Every Baddie\nthat makes it to the bottom of the\nwindow earns you 1 point.",
                                                    fontSize=36, textColor=WHITE)
        self.baddieImage = pygwidgets.Image(self.window, (40, 320), pygame.image.load('images/baddie.png'))

        self.instructions3 = pygwidgets.DisplayText(self.window, (120, 410),
                                                    "Catch the Goodies. Every Goodie\nyou catch is worth 25 points",
                                                    fontSize=36, textColor=WHITE)
        self.goodieImage = pygwidgets.Image(self.window, (40, 410), pygame.image.load('images/goodie.png'))

        # Y 좌표를 350에서 480으로 변경하여 아래로 이동
        self.startButton = pygwidgets.TextButton(self.window, (220, 480), 'Start', fontSize=40)

        # Y 좌표를 420에서 550으로 변경하여 아래로 이동
        self.highScoresButton = pygwidgets.TextButton(self.window, (170, 550), 'Show High Scores', fontSize=40)

        try:
            self.oSound = pygame.mixer.Sound('sounds/background.wav')
            self.oSound.play(-1)  # Loop forever
        except pygame.error as e:
            print(f"Could not load sound: {e}")
            self.oSound = None

    def getSceneKey(self):
        return SCENE_SPLASH

    def enter(self, data):
        if self.oSound:
            self.oSound.play(-1)

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.startButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)
            elif self.highScoresButton.handleEvent(event):
                self.goToScene(SCENE_HIGH_SCORES)

    def update(self):
        pass

    def draw(self):
        self.window.fill(BLACK)
        self.title.draw()
        self.instructions1.draw()
        self.playerImage.draw()
        self.instructions2.draw()
        self.baddieImage.draw()
        self.instructions3.draw()
        self.goodieImage.draw()
        self.startButton.draw()
        self.highScoresButton.draw()

    def leave(self):
        if self.oSound:
            self.oSound.stop()