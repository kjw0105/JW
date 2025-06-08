# HighScoresData class to load, save, and manage high scores
import json
from Constants import *  # HIGH_SCORES_FILE, HIGH_SCORES_TO_KEEP

class HighScoresData():
    def __init__(self):
        self.highScores = []
        self.loadHighScores()

    def addHighScore(self, newScore):
        self.highScores.append(newScore)
        self.highScores.sort(reverse=True)  # Descending order
        self.highScores = self.highScores[:HIGH_SCORES_TO_KEEP]
        self.saveHighScores()

    def loadHighScores(self):
        try:
            with open(HIGH_SCORES_FILE, 'r', encoding='utf-8') as f:
                self.highScores = json.load(f)
                if not isinstance(self.highScores, list):
                    raise ValueError("Invalid data format: not a list")
        except (FileNotFoundError, json.JSONDecodeError, ValueError, UnicodeDecodeError) as e:
            print(f"[INFO] High scores reset to default: {e}")
            self.highScores = [0] * HIGH_SCORES_TO_KEEP
            self.saveHighScores()
        self.highScores.sort(reverse=True)
        self.highScores = self.highScores[:HIGH_SCORES_TO_KEEP]

    def saveHighScores(self):
        try:
            with open(HIGH_SCORES_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.highScores, f)
        except Exception as e:
            print(f"[ERROR] Error saving high scores: {e}")

    def getHighScores(self):
        return self.highScores
