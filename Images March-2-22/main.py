import pygame

pygame.init()

pygame_width = 800
pygame_height = 600

gameDisplay = pygame.display.set_mode((pygame_width,pygame_height))

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

crashed = False

carImg = pygame.image.load('racecar.png')

def car (x, y):
    gameDisplay.blit(carImg, (x, y))

x = (pygame_width * 0.5)
y = (pygame_height * 0.5)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x, y)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
