import pygame, sys, time, random
width = 600
height = 600
bg = (200, 115, 251)

class Ball:
    def __init__(self):
        self.image = pygame.image.load("beach-ball.png")
        self.speed = [random.uniform(-4, 4), 1]
        self.rect = self.image.get_rect()
    def update(self):
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] =- self.speed[1]
            self.speed[0] = random.uniform(-4, 4)
        elif self.rect.left < 0 or self.rect.right > width:
            self.speed[0] =- self.speed[0]
        self.move()

    def move(self):
        self.rect = self.rect.move(self.speed)

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("bomb.png")
        self.speed = [random.uniform(-4, 4), 3]
        self.rect = self.image.get_rect()
    def update(self):
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] =- self.speed[1]
            self.speed[0] = random.uniform(-4, 4)
        elif self.rect.left < 0 or self.rect.right > width:
            self.speed[0] =- self.speed[0]
        self.move()

    def move(self):
        self.rect = self.rect.move(self.speed)

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont("Ariel", 36)
        self.color = ("White")
        self.pos = (10,10)

    def increase(self):
        self.value += 10

    def decrease(self, screen):
        self.value -= 1
        if self.value < -20:
            fin = self.font.render("GAME OVER", True, self.color)
            screen.blit(fin, (200,200))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()

    def render(self, screen):
        score_text = self.font.render("Score: " + str(self.value), True, self.color)
        screen.blit(score_text, self.pos)

def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ball Game")
    ball = Ball()
    enemy = Enemy()
    score = Score()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball.rect.collidepoint(pygame.mouse.get_pos()):
                    ball.speed[0] = random.uniform(4, -4)
                    ball.speed[1] =- 2
                    score.increase()
            elif enemy.rect.collidepoint(pygame.mouse.get_pos()):
                enemy.speed[0] = random.uniform(4, -4)
                enemy.speed[1] =- 2
                score.decrease(screen)
        screen.fill(bg)
        screen.blit(ball.image , ball.rect)
        screen.blit(enemy.image , enemy.rect)
        ball.update()
        enemy.update()
        score.render(screen)
        pygame.display.update()
        clock.tick(60)
main()
