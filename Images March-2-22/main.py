import pygame

pygame.init()

pygame_width = 800
pygame_height = 600

gameDisplay = pygame.display.set_mode((pygame_width,pygame_height))

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

crashed = False

carImg = pygame.image.load('Images March-2-22/racecar.png')

def car (x, y):
    gameDisplay.blit(carImg, (x, y))

x = (pygame_width * 0.5)
y = (pygame_height * 0.5)
x_change = 0
y_change = 0
car_speed = 5

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -10
        elif event.key == pygame.K_RIGHT:
            x_change = 10
        elif event.key == pygame.K_UP:
            y_change = -10
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0

    x += x_change
    y += y_change

    gameDisplay.fill(white)
    car(x, y)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
