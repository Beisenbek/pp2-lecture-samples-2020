# The first half is just boiler-plate stuff...

import pygame

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self, seconds):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    

    active_scene = starting_scene

    while active_scene != None:
        ms = clock.tick(fps)
        sec = ms / 1000

        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update(sec)
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
    
    def Update(self, seconds):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))

class Tank:
    def __init__(self, originX, originY, width, height, speed):
        self.originX = originX
        self.originY = originY
        self.width = width
        self.height = height
        self.direction = 3
        #direction 1 - up, 2 - right, 3 - down, 4 - left, 
        self.speed = speed
        self.stop = True
    
    def ChangeDirection(self, direction):
        self.direction = direction
         
    def UpdateLocation(self, seconds):
        if self.stop == False:
            if self.direction == 1:
                self.originY -= self.speed * seconds
            elif self.direction == 2:
                self.originX += self.speed * seconds
            elif self.direction == 3:
                self.originY += self.speed * seconds
            elif self.direction == 4:
                self.originX -= self.speed * seconds   
    
    def GetRectangle(self):
        return (self.originX, self.originY, self.width, self.height)

    def GetRectangle2(self):
        return (self.originX + self.width/2, self.originY + self.height/2, self.width, 5)


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.tank = Tank(20, 20, 50, 50, 40)

    def ProcessInput(self, events, pressed_keys):
        if pressed_keys[pygame.K_UP]: 
            self.tank.ChangeDirection(1)
        elif pressed_keys[pygame.K_RIGHT]: 
            self.tank.ChangeDirection(2)
        elif pressed_keys[pygame.K_DOWN]:
            self.tank.ChangeDirection(3)
        elif pressed_keys[pygame.K_LEFT]:
            self.tank.ChangeDirection(4)
        
        if pressed_keys[pygame.K_SPACE]:
            if self.tank.stop == True:
                self.tank.stop = False
            else:
                 self.tank.stop = True
        
    def Update(self, seconds):
        self.tank.UpdateLocation(seconds)
    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))
        pygame.draw.rect(screen,(200, 255, 122), self.tank.GetRectangle())
        pygame.draw.rect(screen,(100, 155, 122), self.tank.GetRectangle2())


run_game(400, 300, 60, TitleScene())