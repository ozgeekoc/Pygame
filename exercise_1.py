import pygame
# Mouse'un ucu kareye temas ettiğinde renk değiştiriyor

pygame.init()
win = pygame.display.set_mode((250,250))
rect = pygame.Rect(*win.get_rect().center, 0,0).inflate(100,100)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    point = pygame.mouse.get_pos()
    collide = rect.collidepoint(point)
    color = (255,0,0) if collide else (255,255,255)

    win.fill(0)
    pygame.draw.rect(win, color, rect)
    pygame.display.flip()

pygame.quit()
exit()
