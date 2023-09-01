import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# making the player a character that is rectangle
player = pygame.rect.Rect(300, 250, 10, 10)

run = True
while run:

    # filling the screen black again so it doesnt leave a trail
    screen.fill((0, 0, 0))

    # drawing the rectangle into the screen
    pygame.draw.rect(screen, (255, 0, 0), player)

    # getting the key that was pressed
    key = pygame.key.get_pressed()

    # moving our character
    if key[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player.move_ip(1, 0)
    elif key[pygame.K_UP]:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()