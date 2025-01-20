import pygame

# pygame setup
pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
YELLOW = (150, 150, 0)
SUN_YELLOW = (247, 220, 111)
LIGHT_BLUE = (51, 233, 255)
GREEN = (0, 100, 0)
DARK_GREEN = (20, 90, 50)
RED200 = (200, 0, 0)
RED150 = (150, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(LIGHT_BLUE)

    pygame.draw.rect(screen, GREY, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
    pygame.draw.polygon(screen, GREEN, [(-200, HEIGHT // 2), (300, 200), (800, HEIGHT // 2)])
    pygame.draw.polygon(screen, DARK_GREEN, [(500, HEIGHT // 2), (1000, 250), (1500, HEIGHT // 2)]) # [(ตำแหน่งมุมซ้าย, ตำแหน่งมุมบน, ตำแหน่งมุมขวา)]
    pygame.draw.circle(screen, SUN_YELLOW, (1100, 150), 100)
    pygame.draw.circle(screen, WHITE, (515, 130), 60)
    pygame.draw.circle(screen, WHITE, (465, 150), 60)
    pygame.draw.circle(screen, WHITE, (565, 150), 60)

    pygame.draw.circle(screen, LIGHT_BLUE, (650, 520), 30)
    pygame.draw.circle(screen, SUN_YELLOW, (650, 520), 25)
    pygame.draw.circle(screen, LIGHT_BLUE, (650, 520), 20)
    pygame.draw.rect(screen, BLACK, (620, 505, 30, 15))

    pygame.draw.rect(screen, RED200, (600, 520, 300, 100))
    pygame.draw.rect(screen, RED150, (900, 470, 70, 120))
    pygame.draw.rect(screen, RED200, (400, 550, 200, 70))
    pygame.draw.rect(screen, RED150, (600, 550, 200, 70))
    pygame.draw.rect(screen, WHITE, (900, 450, 70, 20))
    pygame.draw.rect(screen, WHITE, (400, 580, 500, 10))
    pygame.draw.polygon(screen, RED200, [(350, 609), (350, 609), (400, 599), (400, 550)])
    pygame.draw.polygon(screen, RED150, [(300, 629), (300, 619), (400, 589), (400, 619)])
    pygame.draw.polygon(screen, RED150, [(690, 479), (700, 509), (720, 519), (900, 519)])
    pygame.draw.polygon(screen, BLACK, [(310, 619), (400, 590), (400, 599)])

    pygame.draw.circle(screen, BLACK, (480, 590), 50)
    pygame.draw.circle(screen, YELLOW, (480, 590), 40)
    pygame.draw.circle(screen, BLACK, (480, 590), 35)
    pygame.draw.circle(screen, GREY, (480, 590), 30)
    pygame.draw.circle(screen, BLACK, (870, 590), 50)
    pygame.draw.circle(screen, YELLOW, (870, 590), 40)
    pygame.draw.circle(screen, BLACK, (870, 590), 35)
    pygame.draw.circle(screen, GREY, (870, 590), 30)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()