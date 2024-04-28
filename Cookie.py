import pygame, sys
#ekran ayarlama
pygame.init()
size = (640,480)
win = pygame.display.set_mode(size)
pygame.display.set_caption("Cookie Clicker")

#renkler
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
button_bg = pygame.Color(68,93,255)
button_border = pygame.Color(85,50,232)

#zaman
fps = 30
fpsclock = pygame.time.Clock()

cookie_image = pygame.image.load("cookie (1).png")
cookie = 0
cookie_rect = pygame.Rect(25,250,cookie_image.get_width(), cookie_image.get_height())
cps = 0.0
font = pygame.font.SysFont("Arial", 24)

class Item:
    def __init__(self, rect, text, base_price, base_cps_each):
        self.rect = rect
        self.text = text
        self.count = 0
        self.base_price = base_price
        self.cps_each = base_cps_each

    def draw(self, surface):
        pygame.draw.rect(surface, button_bg, self, 0)
        pygame.draw.rect(surface, button_border, self, 2)
        text_surface = font.render(str(self.count) + "x" + self.text + "$" + str(int (self.price())), False, black)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10 , self.rect.top + self.rect.height*0.25)
        surface.blit(text_surface, text_rect)
    def total_cps(self):
        return self.cps_each * self.count
    def price(self):
        return self.base_price * 1.15**self.count
    def click(self):
        price = self.price()
        global cookie
        if cookie >= price:
            self.count += 1
            cookie -= price
    def collidepoint(self, point):
        return self.rect.collidepoint(point)

def make_items(text_list, base_price_list, cps_list, rect, spacing):
    button_height = rect.height / len (text_list)
    button_width = rect.width
    buttons = []
    for i in range(len(text_list)):
        text = text_list[i]
        base_price = base_price_list[i]
        base_cps = cps_list[i]
        button_rect = pygame.Rect(rect.left , rect.top+i*(button_height + spacing), button_width, button_height)

        button = Item(button_rect, text, base_price, base_cps)
        buttons.append(button)
    return buttons

def click_cookie():
    global cookie
    cookie +=1


items = make_items(["Cursor", "Grandma", "Farm", "Mine", "Factory", "Bank"], [15, 100, 500, 3000, 10000, 40000], [0.1, 0.5, 4, 10, 40, 100], pygame.Rect(400, 25, 230, 400), 5)

def calculate_cps():
    global cps
    cps = 0.0
    for item in items:
        cps += item.total_cps()
        cps = round(cps, 3)
    CPS = cps

def update_cookie():
    global cookie
    cookie += cps/fps

while True:
    win.fill(black)
    win.blit(cookie_image, cookie_rect)
    text_surface = font.render(str(int(cookie)) + " + " + str(cps) + " CPS ", False, white)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (100,200)
    win.blit(text_surface, text_rect)
    for button in items:
        button.draw(win)
    calculate_cps()
    update_cookie()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_button = event.button
            if mouse_button == 1:
                for button in items:
                    if button.collidepoint(mouse_pos):
                        button.click()
                        break
                if cookie_rect.collidepoint(mouse_pos):
                    click_cookie()

    pygame.display.update()
    fpsclock.tick(fps)
