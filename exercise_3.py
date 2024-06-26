import pygame
# Mouse'un ucundaki kare, dieğr kareye temas edince... garip şeyler oluyor
pygame.init()
win = pygame.display.set_mode((250,250))
sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((75,75))
sprite1.image.fill((255,0,0))
sprite1.rect = pygame.Rect(*win.get_rect().center,0,0).inflate(75,75)

sprite2 = pygame.sprite.Sprite()
sprite2.image = pygame.Surface((75,75))
sprite2.image.fill((0,255,0))
sprite2.rect = pygame.Rect(*win.get_rect().center,0,0).inflate(75,75)

all_group = pygame.sprite.Group([sprite1, sprite2])
test_group = pygame.sprite.Group(sprite2)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sprite1.rect.center = pygame.mouse.get_pos()
    collide = pygame.sprite.spritecollide(sprite1, test_group, False)
    win.fill(0)
    all_group.draw(win)
    for x in collide:
        pygame.draw.rect(win, (255,255,255), x.rect, 5, 1)
    pygame.display.flip()

pygame.quit()
exit()
