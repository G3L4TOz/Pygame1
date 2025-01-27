import pygame

# pygame setup
pygame.init()
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
X = 0
Y = 0
FX = 2
FY = 2
C = WHITE

isxplus = True
isxminus = False
isyplus = True
isyminus = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(LIGHT_BLUE)

    pygame.draw.rect(screen, GREY, (0, 540, 1280, 540)) #ถนน
    pygame.draw.polygon(screen, GREEN, [(-200, 540), (300, 200), (800, 540)]) #ภูเขาซ้าย
    pygame.draw.polygon(screen, DARK_GREEN, [(500, 540), (1000, 250), (1500, 540)]) #ภูเขาขวา
    pygame.draw.circle(screen, SUN_YELLOW, (1100, 150), 100) #ดวงอาทิตย์
    pygame.draw.circle(screen, WHITE, (515, 130), 60) #เมฆล่าง
    pygame.draw.circle(screen, WHITE, (465, 150), 60) #เมฆซ้าย
    pygame.draw.circle(screen, WHITE, (565, 150), 60) #เมฆขวา

    pygame.draw.circle(screen, LIGHT_BLUE, (650, 520), 30) #หมวกกันน็อค
    pygame.draw.circle(screen, SUN_YELLOW, (650, 520), 25) #ลายหมวกกันน็อค
    pygame.draw.circle(screen, LIGHT_BLUE, (650, 520), 20) #สีทับหมวกกันน็อค
    pygame.draw.rect(screen, BLACK, (620, 505, 30, 15)) #ชิลด์หมวกกันน็อค

    pygame.draw.rect(screen, RED200, (600, 520, 300, 100)) #ตัวถัง
    pygame.draw.rect(screen, RED150, (900, 470, 70, 120)) #ข้างตัวถัง
    pygame.draw.rect(screen, RED200, (400, 550, 200, 70)) #ตัวถังหน้า
    pygame.draw.rect(screen, RED150, (600, 550, 200, 70)) #สปอยเลอร์
    pygame.draw.rect(screen, WHITE, (900, 450, 70, 20)) #ปลายสปอยเลอร์
    pygame.draw.rect(screen, WHITE, (400, 580, 500, 10)) #ลายแถบข้างรถ
    pygame.draw.polygon(screen, RED200, [(350, 609), (350, 609), (400, 599), (400, 550)]) #กันชนหน้า
    pygame.draw.polygon(screen, RED150, [(300, 629), (300, 619), (400, 589), (400, 619)]) #ลิ้นกันชนหน้า
    pygame.draw.polygon(screen, RED150, [(690, 479), (700, 509), (720, 519), (900, 519)]) #ช่องอากาศ
    pygame.draw.polygon(screen, BLACK, [(310, 619), (400, 590), (400, 599)]) #ลายกันชนหน้า

    pygame.draw.circle(screen, BLACK, (480, 590), 50) #ยางหน้า
    pygame.draw.circle(screen, YELLOW, (480, 590), 40) #ลายยางหน้า
    pygame.draw.circle(screen, BLACK, (480, 590), 35) #ทับลายยางหน้า
    pygame.draw.circle(screen, GREY, (480, 590), 30) #ล้อหน้า
    pygame.draw.circle(screen, BLACK, (870, 590), 50) #ยางหลัง
    pygame.draw.circle(screen, YELLOW, (870, 590), 40) #ลายยางหลัง
    pygame.draw.circle(screen, BLACK, (870, 590), 35) #ทับลายยางหลัง
    pygame.draw.circle(screen, GREY, (870, 590), 30) #ล้อหลัง
    
    pygame.draw.rect(screen, C, (X, Y, 100, 100))

    if isxplus and isyplus:
        X = X + FX
        Y = Y + FY
        C = (255, 0, 0)
    if isxplus and isyminus:
        X = X + FX
        Y = Y - FY
        C = (0, 255, 0)
    if isxminus and isyplus:
        X = X - FX
        Y = Y + FY
        C = (0, 0, 255)
    if isxminus and isyminus:
        X = X - FX
        Y = Y - FY
        C = (255, 255, 0)
    if X == 1180:
        isxminus = True
        isxplus = False
    if X == 0:
        isxminus = False
        isxplus = True
    if Y == 620:
        isyminus = True
        isyplus = False
    if Y == 0:
        isyminus = False
        isyplus = True
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()