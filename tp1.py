import pygame
import sys

pygame.init()
background = pygame.image.load("background.png")
screen = pygame.display.set_mode((800, 600))
screen.blit(background, (0,0))
playing = True

tileimg = pygame.image.load('pictures/c1.png')

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.width = 30
        self.height = 40
        self.rect = [x,y]
        
    def move(self):
        self.rect = [400, 300]
        
hand = pygame.sprite.Group()
x = 10
for i in range(14):
    hand.add(Tile(tileimg, x, 30))
    x += 50
    
handiteration = hand.sprites()
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coordinates = pygame.mouse.get_pos()
            if 30 <= coordinates[1] <= 70:
                tileNum = coordinates[0] // 50 - 1
                hand.remove(handiteration[tileNum])
                #handiteration[tileNum].move()
                #hand.add(handiteration[tileNum])
    hand.draw(screen)
    pygame.display.update()
pygame.quit();sys.exit()