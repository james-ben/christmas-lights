import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600
size = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

SCREEN.fill(WHITE)
# pygame.display.flip()
surface = pygame.Surface(size)
surface.fill(WHITE)

radius = 25
# pygame.draw.circle(surface, RED, (radius, radius), radius)
pygame.draw.ellipse(surface, RED, pygame.Rect([(50, 100), (150, 200)]))

points = [(25, 0), (50, 25), (25, 50), (0, 25)]
pygame.draw.lines(surface, GREEN, True, points)

SCREEN.blit(surface, (0, 0))
pygame.display.update()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

pygame.quit()
