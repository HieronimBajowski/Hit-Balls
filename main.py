import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Ustawienia kolorów
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Utworzenie okna gry
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kliknij Kulki")

# Utworzenie obiektu licznika punktów
font = pygame.font.SysFont(None, 30)
score = 0


# Funkcja tworząca nową kulke na losowej pozycji
def new_ball():
    # Wygenerowanie losowej pozycji i koloru kulki
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    start_time = pygame.time.get_ticks()  # Dodanie czasu rozpoczęcia rysowania kulki
    # Narysowanie kulki na ekranie
    pygame.draw.circle(screen, color, (x, y), 30)
    # Zwrócenie pozycji, koloru i czasu rozpoczęcia rysowania kulki
    return (x, y, color, start_time)

# Główna pętla gry
# Główna pętla gry
running = True
clock = pygame.time.Clock()
balls = []
while running:
    # Sprawdzenie zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Sprawdzenie czy kliknięto w kulke
            pos = pygame.mouse.get_pos()
            for ball in balls:
                if ball[0]-30 <= pos[0] <= ball[0]+30 and ball[1]-30 <= pos[1] <= ball[1]+30:
                    # Usunięcie kulki i dodanie punktu
                    balls.remove(ball)
                    score += 1
    # Wyczyszczenie ekranu
    screen.fill(WHITE)

    # Dodanie nowych kulek
    if random.randint(0, 30) == 0:
        balls.append(new_ball())

    # Przefiltrowanie listy kulek i usunięcie starych kulek
    balls = [(x, y, color, start_time) for (x, y, color, start_time) in balls if pygame.time.get_ticks() - start_time < 3000]

    # Narysowanie kulek
    for ball in balls:
        pygame.draw.circle(screen, ball[2], (ball[0], ball[1]), 30)

    # Aktualizacja licznika punktów
    score_text = font.render("Punkty: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Zaktualizowanie ekranu
    pygame.display.update()

    # Ograniczenie liczby klatek na sekundę
    clock.tick(FPS)

# Zakończenie Pygame
pygame.quit()
