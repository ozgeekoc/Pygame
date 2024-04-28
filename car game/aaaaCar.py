import pygame, sys, random, time
from pygame.locals import *
pygame.init()

#oyunun hızı ve zamanı
FPS = 60
time = pygame.time.Clock()

#renkler
blue = (0,0,185)
red = (200,0,0)
green = (0,200,0)
black = (0,0,0)
white = (255,255,255)

bg = (195,195,195)

#font ayarları
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("GAME OVER", True, black)

#arka plan
background = pygame.image.load("AnimatedStreet.png")

#ekran ayarları
width = 400
height = 600
speed = 4
pspeed = 5
score = 0
win = pygame.display.set_mode((width, height))
win.fill(white)
pygame.display.set_caption("Car Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint (40, width-40), 0)
    def move (self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > height):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width-40), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 :
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-pspeed,0)
        if self.rect.right < width :
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(pspeed,0)

    def draw(self,surface):
        surface.blit(self.image, self.rect)

E1 = Enemy()
P1 = Player()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)
pygame.mixer.Sound('background.wav').play()
while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed+=0.3
            pspeed+=0.2
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.fill(bg)
    pygame.display.update
    win.blit(background, (0,0))
    score_screen = font_small.render(str(score), True, black)
    win.blit(score_screen, (10,10))
    for entity in all_sprites:
        win.blit(entity.image , entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1 , enemies):
        pygame.mixer.pause()
        pygame.mixer.Sound('crash.wav').play()
        pygame.time.wait(1000)
        win.fill(red)
        win.blit(game_over, (16,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    time.tick(FPS)
