import pygame, sys
pygame.init()
win = pygame.display.set_mode((300,300))
pygame.display.set_caption("Mouse")
fps_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        print("Sol click")
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        print("Mouse'a basıldı")
    #mouse pozisyonunu verir
    #print(pygame.mouse.get_pos())

    #mouse hareketine göre değerleri verir
    #print(pygame.mouse.get_rel())

    win.fill("Indigo")
    pygame.display.update()
    fps_clock.tick(30)