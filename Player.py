# Player
import pygame
import pygwidgets
from Constants import *

class Player():
    def __init__(self, window):
        self.window = window
        self.image = pygwidgets.Image(window,
                                (-100, -100), 'images/player.png')
        playerRect = self.image.getRect()
        self.maxX = WINDOW_WIDTH - playerRect.width
        self.maxY = GAME_HEIGHT - playerRect.height
        self.health = PLAYER_INITIAL_HEALTH

        # 무적 관련 변수
        self.invincible = False
        self.invincibleStartTime = 0 # pygame.time.get_ticks() 사용 (밀리초 단위)
        self.invincibleDuration = 0 # 무적 지속 시간 (초 단위)
        self.flash_counter = 0 # 무적 상태 깜빡임 효과를 위한 프레임 카운터

        # 체력 회복 효과 관련 변수
        self.heal_effect_timer = 0 # 프레임 단위

    # Every frame, move the Player icon to the mouse position
    def update(self, x, y):
        # 무적 상태 시간 체크
        if self.invincible:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.invincibleStartTime > self.invincibleDuration * 1000: # 초 단위를 밀리초로 변환
                self.invincible = False
            self.flash_counter += 1 # 무적 상태일 때만 카운터 증가

        # 체력 회복 효과 타이머 감소
        if self.heal_effect_timer > 0:
            self.heal_effect_timer -= 1

        if x < 0:
            x = 0
        elif x > self.maxX:
            x = self.maxX
        if y < 0:
            y = 0
        elif y > self.maxY:
            y = self.maxY

        self.image.setLoc((x, y))
        return self.image.getRect()

    def draw(self):
        # 무적 상태일 때 플레이어 아이콘 깜빡임 효과
        if self.invincible:
            # INVINCIBLE_FLASH_INTERVAL 주기로 이미지를 보였다 숨겼다 함
            if (self.flash_counter // INVINCIBLE_FLASH_INTERVAL) % 2 == 0:
                self.image.draw() # 짝수 주기에는 그림 (보임)
            else:
                pass # 홀수 주기에는 그리지 않음 (숨김)
        else:
            self.image.draw() # 무적 상태가 아니면 항상 그림

        # 체력 회복 효과 그리기
        if self.heal_effect_timer > 0:
            playerRect = self.image.getRect()
            # 플레이어 주변에 녹색 테두리 효과 그리기
            effect_rect = pygame.Rect(playerRect.left - HEAL_EFFECT_PADDING,
                                      playerRect.top - HEAL_EFFECT_PADDING,
                                      playerRect.width + (HEAL_EFFECT_PADDING * 2),
                                      playerRect.height + (HEAL_EFFECT_PADDING * 2))
            pygame.draw.rect(self.window, GREEN, effect_rect, 3) # 3은 선 두께

    def takeDamage(self, damage):
        if self.invincible:
            return  # 무적 상태일 땐 데미지 안 받음
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > PLAYER_INITIAL_HEALTH:
            self.health = PLAYER_INITIAL_HEALTH
        self.heal_effect_timer = HEAL_EFFECT_DURATION_FRAMES # 체력 회복 시 효과 타이머 설정

    def getHealth(self):
        return self.health

    def isAlive(self):
        return self.health > 0

    def setInvincible(self, duration_seconds):
        self.invincible = True
        self.invincibleStartTime = pygame.time.get_ticks()
        self.invincibleDuration = duration_seconds # 초 단위 지속 시간
        self.flash_counter = 0 # 깜빡임 타이머 초기화

    def isInvincible(self):
        return self.invincible