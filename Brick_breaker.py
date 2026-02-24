import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker - CodeWithAnnu")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 80, 80)
BLACK = (0, 0, 0)
GREEN = (0, 200, 100)

# Paddle
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 15)
paddle_speed = 8

# Ball
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2, 20, 20)
ball_speed_x = 5 * random.choice([-1, 1])
ball_speed_y = -5

# Bricks
bricks = []
rows = 5
cols = 8
brick_width = WIDTH // cols
brick_height = 30

for row in range(rows):
    for col in range(cols):
        brick = pygame.Rect(
            col * brick_width,
            row * brick_height + 50,
            brick_width - 5,
            brick_height - 5
        )
        bricks.append(brick)

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall collision
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= HEIGHT:
        running = False  # Game Over

    # Paddle collision
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Brick collision
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            break

    # Draw objects
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)

    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)

    pygame.display.flip()

pygame.quit()