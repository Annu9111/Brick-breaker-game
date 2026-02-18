import pygame
import random

pygame.init()
WIDTH,HEIGHT= 800,800

screen=pygame.display.set_mode(WIDTH,HEIGHT)
pygame.dispaly.set_caption("Brick Breaker")

clock=pygame.time.Clock()
WHITE = (255,255,255)
BLUE = (0,150,255)
RED = (255,50,50)
BLACK = (0 , 0 , 0)

paddle = pygame.rect(WIDTH//2-60,HEIGHT-30,120,15)
paddle_speed=8

ball=pygame.rect(WIDTH//2-10,HEIGHT//2,20,20)
ball_speed_x=5*random.choice(1,-1)
ball_speed_y=-5

bricks=[]
rows=5
cols=8
brick_width=WIDTH//cols
brick_heigth=30

for row in range(rows):
    for col in range(cols):
        brick=pygame.Rect(col*brick_width,row*brick_heigth+50,brick_width -5,brick_heigth-5)
        bricks.append(brick)
        
running=True
while running:
    clock.tick(60)
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left>0:
        paddle.x-=paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right<WIDTH:
        paddle.x+=paddle_speed
        
    ball.x+=ball_speed_x
    ball.y+=ball_speed_y
    
    if ball.left<=0 or ball.right>=WIDTH:
        ball_speed_x*=-1
    if ball.top<=0:
        ball_speed_y*=-1
    if ball.bottom>=HEIGHT:
        running=False
        
    if ball.colliderect(paddle):
        ball_speed_y*=-1
        
    for brick in brick[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y*-1
            break
        

                                                  