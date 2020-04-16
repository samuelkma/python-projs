import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Smiley Pong")
keepGoing = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
WHITE = (255,255,255)
timer = pygame.time.Clock()
speedx = 5
speedy = 5
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550
picw = 100
pich = 100
points = 0
lives = 5
font = pygame.font.Sysfont("Times", 24)

while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                points = 0
                lives = 5
                picx = 0
                picy = 0
                speedx = 5
                speedy = 5
                picx += speedx
                picy += speedy

                if picx <= 0 or picy >= 700:
                    speedx = -speedx * 1.1
                if picy <= 0:
                    speedy = -speedy + 1
                if picy >= 500:
                    lives -= 1
                    speedy = -5
                    speedx = 5
                    picy = 499

                screen.fill(BLACK)
                screen.blit(pic, (picx, picy))

                paddlex = pygame.mouse.get_pos()[0]
                paddlex -= paddlew / 2
                pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))

                if picy + pich >= paddley and picy + pich <= paddley + paddleh







                
