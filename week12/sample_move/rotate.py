import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

lineImage = pygame.Surface((50, 50))
pygame.draw.rect(lineImage, (0, 0, 255), (25, 25, 25, 5))

baseTankImage = pygame.Surface((50, 50))
pygame.draw.rect(baseTankImage, (255, 0, 255), (0, 0, 50, 50))

angle = 0
rect = lineImage.get_rect()
rect.center = (125, 125)

while not done:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((255, 255, 255))
        screen.blit(baseTankImage, (100, 100, 50, 50))
        oldCenter = rect.center
        newImage = pygame.transform.rotate(lineImage, angle)
        rect = newImage.get_rect()
        rect.center = oldCenter
        screen.blit(newImage,rect)
        #pygame.draw.rect(screen,(200, 255, 122),(20,20,20,20))
        pygame.display.flip()
        angle = (angle + 1) % 360
       