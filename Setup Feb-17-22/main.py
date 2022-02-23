import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

    
pygame.quit()
quit()