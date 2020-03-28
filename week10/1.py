import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

dx = 3
dy = 3

objectLocationX = 20
objectLocationY = 20

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
        
        screen.blit(get_image('./images/intro_ball.gif'), (objectLocationX, objectLocationY))
        
        pygame.display.flip()
        clock.tick(60)