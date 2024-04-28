from typing import Any
import pygame, sys, random, time
from pygame.locals import *
pygame.init()

vec = pygame.math.Vector2
Height = 400
Width = 450
ACC = 0.5
FRIC =-0.12
FPS = 60

FramePerSec = pygame.time.Clock()
screen = pygame.display.set_mode((Height,Width))
pygame.display.set_caption("Platform Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
        self.pos = vec((10,385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc

        if self.pos.x > Width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Width
        self.rect.midbottom = self.pos

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -15
    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if P1.vel.y>0:
            if hits:
                self.vel.y=0
                self.pos.y=hits[0].rect.top+1

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((Width, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (Height/2, Width-10))

    def move(self):
        pass
def plat_gen():
    while len(platforms) > 7:
        width = random.randrange(50,100)
        p = Platform()
        p.rect.center = (random.randrange(0, Width-width), random.randrange(-50,0))
        platforms.add(p)
        all_sprites.add(p)

PT1 = Platform()
P1 = Player()

PT1.surf = pygame.Surface((Height,20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (Height/2 , Width-10))

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group
platforms.add(PT1)

while True:
    screen.fill("White")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
    P1.update()
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        entity.move()
    pygame.display.update()
    FramePerSec.tick(FPS)
