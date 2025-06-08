# Controls scene
import pygame
import pygwidgets
import pyghelpers
from Constants import *

class SceneControls(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.backgroundImage = pygwidgets.Image(self.window, (0, 0), 'images/controlsBackground.jpg') # Controls background
        self.backButton = pygwidgets.CustomButton(self.window, (WINDOW_WIDTH / 2 - 75, WINDOW_HEIGHT - 100),
                                                   up='images/backNormal.png',
                                                   down='images/backDown.png',
                                                   over='images/backOver.png')
        self.instructionsText = pygwidgets.DisplayText(self.window, (50, 150),
                                                    'Move the player with your mouse to dodge baddies.\n'
                                                    'Collect green goodies to increase your score.\n'
                                                    'Collect red goodies to restore your health.\n'
                                                    'Avoid baddies! Each hit reduces your health.\n'
                                                    'If your health drops to zero, it\'s game over!',
                                                    fontSize=30, textColor=BLACK, width=WINDOW_WIDTH - 100, justified='center')


    def getSceneKey(self):
        return 'scene controls' # Unique key for this scene

    def enter(self, data):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.backButton.handleEvent(event):
                self.goToScene(SCENE_SPLASH)

    def update(self):
        pass

    def draw(self):
        self.backgroundImage.draw()
        self.instructionsText.draw()
        self.backButton.draw()

    def leave(self):
        pass