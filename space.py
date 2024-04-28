import pygame
score = 0
class Game:
    pygame.display.set_caption("SPACE SHOOTER")
    screen = None
    aliens = []
    rockets = []
    lost = False
    score = 0
    def __init__ (self, width, height):
        pygame.init()
        self.width = width 
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        done = False
        hero = Hero(self, width/2, height-30)
        generator = Generator(self)
        rocket = None

        while not done :
            if len(self.aliens) == 0:
                self.screen.fill("Black")
                self.displayText("VICTORY!")
                pygame.display.update()
                pygame.time.wait(3000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x, hero.y))
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                hero.x -= 2 if hero.x> 20 else 0
            elif pressed[pygame.K_RIGHT]:
                hero.x += 2 if hero.x<width -20 else 0
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0,0,0))
            ###self.show_score("Score: " + str(score))
            ###pygame.display.update()
            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)
                if (alien.y>height-60):
                    self.lost = True
                    self.screen.fill("Black")
                    self.displayText("YOU LOST.")
                    pygame.display.update()                   
            for rocket in self.rockets:
                rocket.draw()
            if not self.lost:
                hero.draw()

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont("Ariel", 50)
        textsurface = font.render(text, False, (44, 0 , 62))
        self.screen.blit(textsurface, (110,160))
    
    ###def show_score(self, text_):
        ##score_f = pygame.font.SysFont("Ariel", 20)
        ##score_s = score_f.render(text_ , True, (255,255,255))
        ##self.screen.blit(score_s, (20,20))

class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.size = 30
    def draw(self):
        pygame.draw.rect(self.game.screen, (81,43,88), pygame.Rect(self.x , self.y , 30 , 30))
        self.y += 0.2
    def checkCollision(self, game):
        for rocket in game.rockets:
            if rocket.x < self.x+self.size and rocket.x > self.x-self.size and rocket.y < self.y+self.size and rocket.y > self.y-self.size:
                game.rockets.remove(rocket)
                game.aliens.remove(self)
                game.score += 10
                
class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
    def draw(self):
        pygame.draw.rect(self.game.screen, (210,250,251), pygame.Rect(self.x , self.y , 10 , 15))

class Generator:
    def __init__(self, game):
        margin = 30
        width = 50 
        for x in range (margin, game.width - margin, width):
            for y in range(margin, int(game.height//2), width):
                game.aliens.append(Alien(game, x, y))
        self.score = 0
        self.game = game

class Rocket:
    def __init__(self, game, x, y):
        self.x=x
        self.y=y
        self.game = game
    def draw(self):
        pygame.draw.rect(self.game.screen, (254, 12, 11), pygame.Rect(self.x, self.y, 5, 7))
        self.y -= 2

if __name__ == '__main__':
    game = Game(600,400)
    pygame.display.update()