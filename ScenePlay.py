# ScenePlay.py
import pygame
import pygwidgets
import pyghelpers
import random

from Constants import *
from Player import *
from ItemMgr import *  # 통합 매니저 사용

class Rectangle():
    def __init__(self, window, rect, fillColor, borderWidth=0, borderColor=None):
        self.window = window
        self.rect = pygame.Rect(rect)
        self.fillColor = fillColor
        self.borderWidth = borderWidth
        self.borderColor = borderColor if borderColor else fillColor 

    def draw(self):
        if self.borderWidth > 0:
            pygame.draw.rect(self.window, self.borderColor, self.rect, self.borderWidth)
            innerRect = self.rect.inflate(-2 * self.borderWidth, -2 * self.borderWidth)
            pygame.draw.rect(self.window, self.fillColor, innerRect, 0)
        else:
            pygame.draw.rect(self.window, self.fillColor, self.rect, 0)

    def setWidth(self, newWidth):
        self.rect.width = newWidth

    def setColor(self, newColor):
        self.fillColor = newColor


class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        # 배경 이미지
        raw_background_image = pygame.image.load('images/playBackground.jpg')
        scaled_background_image = pygame.transform.scale(raw_background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.backgroundImage = pygwidgets.Image(self.window, (0, 0), scaled_background_image)

        self.oPlayer = Player(self.window)
        self.playerRect = self.oPlayer.update(WINDOW_WIDTH // 2, GAME_HEIGHT // 2)
        self.oItemMgr = ItemMgr(self.window)  # 통합 매니저

        self.score = 0
        self.scoreText = pygwidgets.DisplayText(self.window, (400, 570), 
                                                 'Score: ' + str(self.score),
                                                 fontSize=48, textColor=WHITE)
        
        # 체력 바
        self.healthBarOutline = Rectangle(self.window,
                                                     (HEALTH_BAR_OFFSET_X, HEALTH_BAR_OFFSET_Y, 
                                                      HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT),
                                                     WHITE, 2)
        self.healthBarFill = Rectangle(self.window,
                                                 (HEALTH_BAR_OFFSET_X, HEALTH_BAR_OFFSET_Y,
                                                  HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT),
                                                 GREEN)
        self.healthText = pygwidgets.DisplayText(self.window, (HEALTH_BAR_OFFSET_X, HEALTH_BAR_OFFSET_Y - 30),
                                                 'Health: ' + str(self.oPlayer.getHealth()),
                                                 fontSize=24, textColor=WHITE)

        self.level = 1
        self.frames_in_level = 0

        # 효과음/음악 (실제 파일 없으면 try-except 처리 권장)
        self.loseSound = pygame.mixer.Sound('sounds/lose.wav')
        self.getGoodieSound = pygame.mixer.Sound('sounds/get_goodie.wav')
        try:
            self.invincibleHitSound = pygame.mixer.Sound('sounds/invincible_hit.wav')
            self.invincibleHitSound.set_volume(0.6)
        except:
            self.invincibleHitSound = None

        try:
            self.backgroundMusic = pygame.mixer.Sound('sounds/background.wav')
            self.backgroundMusic.set_volume(0.3)
        except:
            self.backgroundMusic = None

        try:
            self.invincibleBackgroundMusic = pygame.mixer.Sound('sounds/invincible_background.wav')
            self.invincibleBackgroundMusic.set_volume(0.4)
        except:
            self.invincibleBackgroundMusic = None

        self.wasInvincibleLastFrame = False

    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, data):
        self.oItemMgr.reset()
        self.oPlayer = Player(self.window)
        self.score = 0
        self.scoreText.setValue('Score: ' + str(self.score))
        self.level = 1
        self.frames_in_level = 0
        if self.backgroundMusic:
            self.backgroundMusic.play(-1)
        if self.invincibleBackgroundMusic:
            self.invincibleBackgroundMusic.stop()
        self.wasInvincibleLastFrame = False
        self.playerRect = self.oPlayer.update(WINDOW_WIDTH // 2, GAME_HEIGHT // 2)

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if event.type == pygame.MOUSEMOTION:
                self.playerRect = self.oPlayer.update(event.pos[0], event.pos[1])

    def update(self):
        # 무적/일반 음악 전환
        currentInvincible = self.oPlayer.isInvincible()
        if currentInvincible and not self.wasInvincibleLastFrame:
            if self.backgroundMusic:
                self.backgroundMusic.stop()
            if self.invincibleBackgroundMusic:
                self.invincibleBackgroundMusic.play(-1)
        elif not currentInvincible and self.wasInvincibleLastFrame:
            if self.invincibleBackgroundMusic:
                self.invincibleBackgroundMusic.stop()
            if self.backgroundMusic:
                self.backgroundMusic.play(-1)
        self.wasInvincibleLastFrame = currentInvincible

        # 레벨업 처리
        self.frames_in_level += 1
        if self.frames_in_level % LEVEL_UP_INTERVAL == 0:
            self.level += 1

        game_level_factor = (self.level - 1) * 0.1

        # 아이템 관리 및 충돌 체크
        hitTypes = self.oItemMgr.update(self.playerRect, game_level_factor)
        for type_, item in hitTypes:
            if type_ == 'baddie':
                if self.oPlayer.isInvincible():
                    if self.invincibleHitSound:
                        self.invincibleHitSound.play()
                else:
                    self.oPlayer.takeDamage(10)
                    self.loseSound.play()
                    if not self.oPlayer.isAlive():
                        if self.backgroundMusic:
                            self.backgroundMusic.stop()
                        if self.invincibleBackgroundMusic:
                            self.invincibleBackgroundMusic.stop()
                        # 점수 기록, 게임오버 씬 전환 등 처리
                        highScoresData = self.request(SCENE_HIGH_SCORES, HIGH_SCORES_DATA)
                        highestScore = highScoresData['highest']
                        lowestScore = highScoresData['lowest']
                        if self.score > lowestScore:
                            self.goToScene(SCENE_HIGH_SCORES, self.score)
                        else:
                            self.goToScene(SCENE_HIGH_SCORES)
            elif type_ == 'score':
                self.score += POINTS_FOR_GOODIE
                self.getGoodieSound.play()
                self.scoreText.setValue('Score: ' + str(self.score))
            elif type_ == 'health':
                self.oPlayer.heal(HEALTH_FOR_GOODIE)
                self.getGoodieSound.play()
            elif type_ == 'shield':
                self.oPlayer.setInvincible(SHIELD_DURATION_SECONDS)
                self.getGoodieSound.play()

        # 체력바 색/크기 조정
        current_health_percent = self.oPlayer.getHealth() / PLAYER_INITIAL_HEALTH
        if current_health_percent > 0.6:
            self.healthBarFill.setColor(GREEN)
        elif current_health_percent > 0.3:
            self.healthBarFill.setColor(BLUE)
        else:
            self.healthBarFill.setColor(RED)
        self.healthBarFill.setWidth(int(HEALTH_BAR_WIDTH * current_health_percent))
        self.healthText.setValue('Health: ' + str(self.oPlayer.getHealth()))

    def draw(self):
        self.backgroundImage.draw()
        self.oPlayer.draw()
        self.oItemMgr.draw()
        self.scoreText.draw()
        self.healthBarFill.draw()
        self.healthBarOutline.draw()
        self.healthText.draw()

    def leave(self):
        if self.backgroundMusic:
            self.backgroundMusic.stop()
        if self.invincibleBackgroundMusic:
            self.invincibleBackgroundMusic.stop()
