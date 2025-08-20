import pygame

pygame.init()

screen = pygame.display.set_mode((640,640))

blackBishop = pygame.image.load('blackBishop.png').convert()

running = True 
x = 0

while running:

    screen.blit(blackBishop, (x, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

