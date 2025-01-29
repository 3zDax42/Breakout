import pygame
import random
pygame.init()
class Brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        if self.ypos == 100:
            self.color = (0, 0, 200)
            self.points_gained = 0
        elif self.ypos == 75:
            self.color = (0, 200, 0)
            self.points_gained = 1
        elif self.ypos == 50:
            self.color = (200, 200, 0)
            self.points_gained = 3
        elif self.ypos == 25:
            self.color = (200, 100, 0)
            self.points_gained = 5
        else:
            self.color = (200, 0, 0)
            self.points_gained = 7
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 50, 25))
    def collision(self, bx, by):
        if not self.isDead:
            if (bx + 5 > self.xpos and bx - 5 < self.xpos + 50) and (by + 5 > self.ypos and by - 5 < self.ypos + 25):
                self.isDead = True
                return True
        return False
    def score(self):
        if self.isDead:
            return int(self.points_gained)
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Breakout")
doExit = False
clock = pygame.time.Clock()
PaddleXpos = 200; PaddleYpos = 450#paddle cordanites
bx = 350; by = 250 #ball position
bVx = 4; bVy = -4 #ball velocity
game_score = 0
WHITE = (255,255,255)
Brick_list = []
for i in range (5):
    for j in range (14):
        Brick_list.append(Brick(j*50,i*25))

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
            game_score += Brick_list[i].score()
    #--------------Render section--------------#
    screen.fill((0,0,0))
    for i in range(len(Brick_list)):
        Brick_list[i].draw()
    pygame.draw.rect(screen,(WHITE), (PaddleXpos, PaddleYpos, 100, 20), 2)
    pygame.draw.circle(screen,(WHITE), (bx, by), 5)
    font = pygame.font.Font(None, 74)
    text = font.render(str(game_score), 1,(WHITE))
    screen.blit(text, (250,50))
    pygame.display.flip()
pygame.quit() #when game is done close down pygame
