import pygame

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Sus Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
playerAsset = pygame.image.load('Player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerAsset, (x, y))


# Game loop
running = True
while running:

    # Draw background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print("Chat, a key was pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Draw Player
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()
