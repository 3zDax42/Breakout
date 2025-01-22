import pygame
import random
pygame.init()
class Brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100, 250), random.randrange(100, 250), random.randrange(100, 250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))
    def collision(self, bx, by):
        if not self.isDead:
            if (bx + 5 > self.xpos and bx - 5 < self.xpos + 100) and (by + 5 > self.ypos and by - 5 < self.ypos + 50):
                self.isDead = True
                return True
        return False
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Breakout")
doExit = False
clock = pygame.time.Clock()
PaddleXpos = 200; PaddleYpos = 450#paddle cordanites
bx = 350; by = 250 #ball position
bVx = 5; bVy = 5 #ball velocity
WHITE = (255,255,255)
Brick_list = []
for i in range (3):
    for j in range (6):
        Brick_list.append(Brick(j*105+38,i*55+10))

while not doExit: #event queue stuff
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
    #--------------Game section---------------#
    keys = pygame.key.get_pressed()
    bx += bVx; by += bVy
    if bx - 5 < 0 or bx + 5 > 700:
        bVx *= -1
    if by < 0 or by + 10 > 500:
        bVy *= -1
    if (bx > PaddleXpos and bx < PaddleXpos + 100) and (by+5 > PaddleYpos and by-5 < PaddleYpos + 20):
        bVy *= -1
    if keys[pygame.K_LEFT]: PaddleXpos -= 10
    if keys[pygame.K_RIGHT]: PaddleXpos += 10
    for i in range(len(Brick_list)):
        if Brick_list[i].collision(bx, by):
            bVy *= -1
    #--------------Render section--------------#
    screen.fill((0,0,0))
    for i in range(len(Brick_list)):
        Brick_list[i].draw()
    pygame.draw.rect(screen,(WHITE), (PaddleXpos, PaddleYpos, 100, 20), 2)
    pygame.draw.circle(screen,(WHITE), (bx, by), 5)
    pygame.display.flip()
pygame.quit() #when game is done close down pygame
