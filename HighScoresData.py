# HighScoresData class
from Constants import *
from pathlib import Path
import json

class HighScoresData():
    """The data file is stored as a list of lists in JSON format.
    Each list is made up of a name and a score:
        [[name, score], [name, score], [name, score] ...]
    In this class, all scores are kept in self.scoresList
    The list is kept in order of scores, highest to lowest.
    """
    def __init__(self):
        self.BLANK_SCORES_LIST = N_HIGH_SCORES * [['-----', 0]]
        self.oFilePath = Path('HighScores.json')

        try:
            data = self.oFilePath.read_text(encoding='utf-8')
            try:
                self.scoresList = json.loads(data)
            except json.JSONDecodeError as e:
                print(f"Error parsing HighScores.json: {e}")
                self.resetScores()
        except FileNotFoundError:
            self.resetScores()
            return
        except UnicodeDecodeError as e:
            print(f"Error reading HighScores.json (encoding): {e}")
            self.resetScores()
        return



    def addHighScore(self, name, newHighScore):
        # Find the appropriate place to add the new high score
        placeFound = False
        for index, nameScoreList in enumerate(self.scoresList):
            thisScore = nameScoreList[1]
            if newHighScore > thisScore:
                # Insert into proper place, remove last entry
                self.scoresList.insert(index, [name, newHighScore])
                self.scoresList.pop(N_HIGH_SCORES)
                placeFound = True
                break
        if not placeFound:
            return  # score does not belong in the list

        # Save the updated scores
        self.saveScores()

    def saveScores(self):
        scoresAsJson = json.dumps(self.scoresList)
        self.oFilePath.write_text(scoresAsJson)

    def resetScores(self):
        self.scoresList = self.BLANK_SCORES_LIST.copy()
        self.saveScores()

    def getScoresAndNames(self):
        namesList = []
        scoresList = []
        for nameAndScore in self.scoresList:
            thisName = nameAndScore[0]
            thisScore = nameAndScore[1]
            namesList.append(thisName)
            scoresList.append(thisScore)

        return scoresList, namesList

    def getHighestAndLowest(self):
        # Element 0 is highest entry, element -1 is the lowest
        highestEntry = self.scoresList[0]
        lowestEntry = self.scoresList[-1]
        # Get the score (element 1) of each sublist
        highestScore = highestEntry[1]
        lowestScore = lowestEntry[1]
        return highestScore, lowestScore

