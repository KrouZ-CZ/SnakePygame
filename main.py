import pygame
import random
from sys import exit
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake game")

FPS = int(100-(W*H/10000))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def init():
    global snake, frut, DIR, score
    snake = [[4, 3], [3, 3], [2, 3]]
    frut = [random.randint(0, W/10-1), random.randint(0, H/10-1)]
    DIR = "Right"
    score = 0

def draw():
    sc.fill(WHITE)
    for i in snake:
        pygame.draw.rect(sc, GREEN, (i[0]*10, i[1]*10, 10, 10))
    pygame.draw.rect(sc, RED, (frut[0]*10, frut[1]*10, 10, 10))
    # draw text
    font = pygame.font.Font(None, 25)
    text = font.render(f'Score: {score}', True, BLACK)
    text_rect = text.get_rect(center=(W/2, 10))
    sc.blit(text, text_rect)
    pygame.display.update()
def count():
    global frut, score
    if frut == snake[0]:
        temp_1 = True
        while temp_1:
            temp_1 = False
            frut = [random.randint(0, W/10-1), random.randint(0, H/10-1)]
            for item in snake:
                if item == frut:
                    temp_1 = True
        snake.append(snake[len(snake) - 1])
        score += 1
def ban():
    sc.fill(WHITE)
    # draw text
    font = pygame.font.Font(None, 50)
    text = font.render("Game over", True, RED)
    text_rect = text.get_rect(center=(W/2, H/2-50))
    sc.blit(text, text_rect)
    # draw text
    font = pygame.font.Font(None, 25)
    text = font.render(f'Score: {score}', True, BLACK)
    text_rect = text.get_rect(center=(W/2, H/2))
    sc.blit(text, text_rect)
    # button
    button = pygame.Surface((100, 50))
    button.fill(WHITE)
    pygame.draw.rect(button, RED, button.get_rect(), 5)
    font = pygame.font.Font(None, 25)
    text = font.render('Restart', True, (0, 0, 0))
    text_rect = text.get_rect(center=(50, 25))
    button.blit(text, text_rect)
    temp = button.get_rect(center=(W/2, H/2+50))
    sc.blit(button, temp)
    pygame.display.update()
    gm = True
    while gm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif event.key == pygame.K_RETURN:
                    gm = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    recter = button.get_rect(center=(W/2, H/2+50))
                    if event.pos[0] > recter.left and event.pos[1] > recter.top and event.pos[0] < recter.right and event.pos[1] < recter.bottom:
                        gm = False
    init()
def collision():
    global snake
    temp = len(snake) - 1
    while temp > 0:
        if snake[temp] == snake[0]:
            ban()
            break
        temp -= 1
    if snake[0][0] < 0: snake[0][0] = W/10-1
    elif snake[0][1] < 0: snake[0][1] = H/10-1
    elif snake[0][0] > W/10: snake[0][0] = 0
    elif snake[0][1] > H/10: snake[0][1] = 0
def move():
    count = len(snake) - 1
    if DIR == "Right":
        while count > 0:
            snake[count] = snake[count-1]
            count -= 1
        snake[0] = [snake[0][0] + 1, snake[0][1]]
    elif DIR == "Left":
        while count > 0:
            snake[count] = snake[count-1]
            count -= 1
        snake[0] = [snake[0][0] - 1, snake[0][1]]
    elif DIR == "Up":
        while count > 0:
            snake[count] = snake[count-1]
            count -= 1
        snake[0] = [snake[0][0], snake[0][1] - 1]
    elif DIR == "Down":
        while count > 0:
            snake[count] = snake[count-1]
            count -= 1
        snake[0] = [snake[0][0], snake[0][1] + 1]
init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_DOWN:
                DIR = "Down"
            elif event.key == pygame.K_UP:
                DIR = "Up"
            elif event.key == pygame.K_LEFT:
                DIR = "Left"
            elif event.key == pygame.K_RIGHT:
                DIR = "Right"
    move()
    count()
    collision()
    draw()
    pygame.time.delay(FPS)
