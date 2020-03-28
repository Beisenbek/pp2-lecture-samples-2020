import pygame
import os


pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

dx = 3
dy = 3

playerImage = pygame.image.load('./images/intro_ball.gif')

objectLocationX = 20
objectLocationY = 20

#pygame.mixer.music.load('./sounds/hit.mp3')
#pygame.mixer.music.play(-1)

music = pygame.mixer.music.load('./sounds/hit.wav')
pygame.mixer.music.play(-1)


#effect = pygame.mixer.Sound('./sounds/foo.mp3')
#effect.play()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            objectLocationY -= dy
        elif pressed[pygame.K_DOWN]: 
            objectLocationY += dy
        elif pressed[pygame.K_LEFT]:
            objectLocationX -= dx
        elif pressed[pygame.K_RIGHT]: 
            objectLocationX += dx

        screen.fill((255, 255, 255))
        
        screen.blit(playerImage, (objectLocationX, objectLocationY))
        
        pygame.display.flip()
        clock.tick(60)