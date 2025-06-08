# High scores scene
import pygame
import pygwidgets
import pyghelpers
from Constants import * # All high scores related constants are here
from HighScoresData import * # For HighScoresData class

class SceneHighScores(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.oHighScoresData = HighScoresData() # Load existing high scores

        self.titleText = pygwidgets.DisplayText(self.window, (0, 50),
                                                 'High Scores',
                                                 fontSize=60, textColor=WHITE,
                                                 width=WINDOW_WIDTH, justified='center')

        self.scoreLabels = []
        # Create DisplayText objects for each high score slot
        for i in range(HIGH_SCORES_TO_KEEP):
            aLabel = pygwidgets.DisplayText(self.window, (0, 0), '', 
                                             fontSize=40, textColor=WHITE,
                                             width=WINDOW_WIDTH, justified='center')
            self.scoreLabels.append(aLabel)

        # Positioning the score labels
        currentY = 150
        for oLabel in self.scoreLabels:
            # === 수정된 줄: 위치를 튜플 (0, currentY)로 전달합니다 ===
            oLabel.setLoc((0, currentY)) 
            currentY = currentY + 50 # Spacing between scores

        self.backButton = pygwidgets.TextButton(self.window, (250, 550), 'Back',
                                                 fontSize=30)
    
    def getSceneKey(self):
        return SCENE_HIGH_SCORES

    def enter(self, data):
        # Data contains the new score if coming from game over
        # If 'data' is an integer, it's a new score to add
        if isinstance(data, int):
            self.oHighScoresData.addHighScore(data)

        highScores = self.oHighScoresData.getHighScores()

        # Populate the DisplayText labels with current high scores
        for i, score in enumerate(highScores):
            if i < HIGH_SCORES_TO_KEEP: 
                self.scoreLabels[i].setValue(str(score))

        # If there are fewer scores than HIGH_SCORES_TO_KEEP, clear remaining labels
        for i in range(len(highScores), HIGH_SCORES_TO_KEEP):
            self.scoreLabels[i].setValue('') 

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.backButton.handleEvent(event):
                self.goToScene(SCENE_SPLASH) # Go back to the splash screen

    def update(self):
        pass

    def draw(self):
        self.window.fill(BLACK)
        self.titleText.draw()
        for oLabel in self.scoreLabels:
            oLabel.draw()
        self.backButton.draw()

    def respond(self, requestID):
        if requestID == HIGH_SCORES_DATA:
            all_scores = self.oHighScoresData.getHighScores()
            
            highestScore = all_scores[0] if all_scores else 0
            lowestScore = all_scores[-1] if all_scores else 0 
            
            return {'highest': highestScore, 'lowest': lowestScore}
        return None