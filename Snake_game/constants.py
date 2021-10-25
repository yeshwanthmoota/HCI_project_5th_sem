

# Creating the game with no borders
FPS = 10


SNAKE_NODE_SIDE = 20
SNAKE_SPEED = 20
# Snake Node side should always be equal to snake speed for continuity of the snake structure
SNAKE_BIRTH_LENGTH = 3
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4



# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 120, 0)



EASY = [800, 600, 12] # 7 is in seconds
HARD = [400, 400, 7] # 12 is in seconds


GAME_LEVEL = HARD
WIDTH = GAME_LEVEL[0]
HEIGHT = GAME_LEVEL[1]
FOOD_MAX_TIME_LIMIT = GAME_LEVEL[2]

SCORE = 0