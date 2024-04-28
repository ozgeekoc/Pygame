import pygame
# Mouse'un ucundaki kare, diğer kareye temas edince renk değiştiriyor

pygame.init()
win = pygame.display.set_mode((250,250))
rect = pygame.Rect(*win.get_rect().center, 0,0).inflate(100,100)
rect2 = pygame.Rect(0,0,75,75)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect2.center = pygame.mouse.get_pos()
    collide = rect.colliderect(rect2)
    color = (255,0,0) if collide else (255,255,255)

    win.fill(0)
    pygame.draw.rect(win, color, rect)
    pygame.draw.rect(win, (0,255,0), rect2, 6, 1)
    pygame.display.flip()

pygame.quit()
exit()
