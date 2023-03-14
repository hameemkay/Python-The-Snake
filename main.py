import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Snake Game"
FPS = 30
font = pygame.font.Font(None, 36)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                 random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
food_spawned = True
direction = "RIGHT"
change_direction = direction
score = 0

# Set up the window display
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# Game Loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_direction = "RIGHT"
            elif event.key == pygame.K_LEFT:
                change_direction = "LEFT"
            elif event.key == pygame.K_UP:
                change_direction = "UP"
            elif event.key == pygame.K_DOWN:
                change_direction = "DOWN"

    # Update the snake's direction
    if change_direction == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    elif change_direction == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_direction == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_direction == "DOWN" and direction != "UP":
        direction = "DOWN"

    # Move the snake
    if direction == "RIGHT":
        snake_position[0] += 10
    elif direction == "LEFT":
        snake_position[0] -= 10
    elif direction == "UP":
        snake_position[1] -= 10
    elif direction == "DOWN":
        snake_position[1] += 10

    # Spawn food
    if not food_spawned:
        food_position = [random.randrange(1, (WINDOW_WIDTH//10)) * 10,
                         random.randrange(1, (WINDOW_HEIGHT//10)) * 10]
    food_spawned = False

    # Check for collision with food
    if snake_position == food_position:
        food_spawned = True
        score += 1
        snake_body.append(list(snake_position))

    # Move the snake's body
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i] = snake_body[i - 1].copy()
    snake_body[0] = snake_position.copy()

    # Check for collision with walls
    if snake_position[0] < 0 or snake_position[0] > WINDOW_WIDTH - 10:
        game_over = True
    elif snake_position[1] < 0 or snake_position[1] > WINDOW_HEIGHT - 10:
        game_over = True

    # Check for collision with snake's
