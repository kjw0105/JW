# Constants for Dodger game

# Window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

# Game area (play area below the score/health bar)
GAME_HEIGHT = 560

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0) # 쉴드 효과를 위한 색상 추가

# Game speed/frame rate
FRAMES_PER_SECOND = 60 # <--- 새로 추가된 부분: 초당 프레임 수

# Player constants
PLAYER_INITIAL_HEALTH = 100
PLAYER_SPEED = 6

# Baddie constants
BADDIE_MIN_SPEED = 2
BADDIE_MAX_SPEED = 8
BADDIE_MIN_SIZE = 10
BADDIE_MAX_SIZE = 40
BADDIE_ADD_NEW_FREQ = 6  # Add a new baddie every this many frames
BADDIE_ADD_NEW_RATE = 0.5  # Lower means more frequent

# Goodie constants
GOODIE_MIN_SIZE = 15
GOODIE_MAX_SIZE = 30
GOODIE_ADD_NEW_FREQ = 10  # Add a new goodie every this many frames
GOODIE_ADD_NEW_RATE = 0.8  # Lower means more frequent
GOODIE_RATE_DECREMENT = 0.01  # This constant controls how goodie rate speeds up

# New Goodie Types
GOODIE_TYPE_SCORE = 'score'
GOODIE_TYPE_HEALTH = 'health'
GOODIE_TYPE_SHIELD = 'shield' # 쉴드 굿디 타입 추가

# Shield constants
SHIELD_DURATION_SECONDS = 5 # 쉴드 유지 시간 (초)
INVINCIBLE_FLASH_INTERVAL = 10 # 무적 상태 깜빡임 주기 (프레임)

# Health bar constants
HEALTH_BAR_OFFSET_X = 20
HEALTH_BAR_OFFSET_Y = WINDOW_HEIGHT - 120 # Adjust Y position as needed
HEALTH_BAR_WIDTH = 150
HEALTH_BAR_HEIGHT = 20

# Healing effect constant
HEAL_EFFECT_DURATION_FRAMES = 60 # 체력 회복 시 효과 지속 시간 (프레임) - 60프레임 = 1초
HEAL_EFFECT_PADDING = 5 # 체력 회복 효과 테두리 패딩

# Leveling constants
LEVEL_UP_INTERVAL = 600 # 600프레임마다 레벨 업 (약 10초)

# Points and Health for collecting goodies
POINTS_FOR_GOODIE = 25
HEALTH_FOR_GOODIE = 10

# Points for evading baddies
POINTS_FOR_BADDIE_EVADED = 10

# High scores constants
HIGH_SCORES_TO_KEEP = 5
HIGH_SCORES_FILE = 'HighScores.json'

# Scene keys
SCENE_SPLASH = 'splash'
SCENE_PLAY = 'play'
SCENE_HIGH_SCORES = 'high_scores'
SCENE_CONTROLS = 'controls'  # For future use

# Data keys for scene communication
HIGH_SCORES_DATA = 'high_scores_data'