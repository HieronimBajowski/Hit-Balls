import pygame
import random

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kliknij Kulki")


font = pygame.font.SysFont(None, 30)
score = 0



def new_ball():
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    start_time = pygame.time.get_ticks()  # Dodanie czasu rozpoczęcia rysowania kulki
    pygame.draw.circle(screen, color, (x, y), 30)
    return (x, y, color, start_time)

running = True
clock = pygame.time.Clock()
balls = []
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          
            pos = pygame.mouse.get_pos()
            for ball in balls:
                if ball[0]-30 <= pos[0] <= ball[0]+30 and ball[1]-30 <= pos[1] <= ball[1]+30:
                  
                    balls.remove(ball)
                    score += 1
    
    screen.fill(WHITE)

    
    if random.randint(0, 30) == 0:
        balls.append(new_ball())


    balls = [(x, y, color, start_time) for (x, y, color, start_time) in balls if pygame.time.get_ticks() - start_time < 3000]

    for ball in balls:
        pygame.draw.circle(screen, ball[2], (ball[0], ball[1]), 30)

    score_text = font.render("Punkty: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()


    clock.tick(60)


pygame.quit()
