import pygame, random 
pygame.init()

Width, Height = 600, 500
black = (0,0,0)
white = (255,255,255)
green = (0,160,0)
red = (200,0,0)

font = pygame.font.Font("freesansbold.ttf", 15)
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Block Game")

clock = pygame.time.Clock()
FPS = 30
class Striker:
    def __init__(self, posx, posy,width,height,speed,color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height= height
        self.color = color
        self.speed = speed
        self.strikerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.striker = pygame.draw.rect(screen, self.color, self.strikerRect)  
    def display(self):
        self.striker = pygame.draw.rect(screen, self.color, self.strikerRect)   
    def update (self, xFac):
        self.posx += self.speed*xFac
        if self.posx <= 0: 
            self.posx= 0 
        elif self.posx +self.width >= Width:
            self.posx = Width- self.width
        self.strikerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)   
        
    def getRect(self):
        return self.strikerRect       
     
class Block:
    def __init__(self, posx, posy, width, height, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self. height= height
        self.color = color
        self.damage = 100
        if color  == white :
            self.health = 200
        else :
            self.health= 100
        self.blockRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.block = pygame.draw.rect(screen, self.color, self.blockRect)
        
    def display(self):
        if self.health > 0:
            self.brick = pygame.draw.rect(screen, self.color, self.blockRect)
    def hit (self):
        self.health -= self.damage
    
    def getRect(self):
        return self.blockRect
    
    def getHealth(self):
        return self.health

class Ball: 
    def __init__( self, posx, posy,radius,speed,color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self. speed= speed
        self.color = color
        self.xFac = 1
        self.yFac =1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius )

    def display( self):
         self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius )
    
    def update (self):
        self.posx += self.xFac*self.speed
        self.posy += self.yFac*self.speed
        if self.posx<= 0 or self.posx >= Width:
            self.xFac *=-1
        if self.posy<= 0:
            self.yFac *=-1
        if self.posy >= Height:
            return True 
        
        return False 
    
    def reset(self):
        self.posx = 0
        self.posy = Height
        self.xFac = 1
        self.yFac = -1

    def hit (self):
        self.yFac *=-1
    
    def getRect (self):
        return self.ball
    
def collisionChecker(rect, ball):
    if pygame.Rect.colliderect(rect,ball):
        return True
    return False

def populateBlocks(blockwidth, blockheight, horizontalGap, verticalGap):
    listOfBlocks=[]
    for i in range (0, Width, blockwidth+horizontalGap):
        for j in range(0, Height//2, blockheight+verticalGap):
            listOfBlocks.append(Block(i, j, blockwidth, blockheight, random.choice([white, green])))
    return listOfBlocks

def gameOver():
    while gameOver: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    return True
            
def main():
    running = True 
    lives = 3
    score = 0

    scoreText = font.render("Score", True, white)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.center = (20, Height-10)

    livesText = font.render("Lives", True, white)
    livesTextRect = livesText.get_rect()
    livesTextRect.center = (120, Height-10)

    striker = Striker(0, Height-50, 100, 20, 10, white)
    strikerXFac = 0
    ball = Ball (20, Height-150, 7, 5, white)
    blockWidth, blockHeight = 40, 15 
    horizontalGap, verticalGap = 20, 20
    listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)
    while running:
        screen.fill(black)
        screen.blit (scoreText, scoreTextRect)
        screen.blit(livesText, livesTextRect)
        scoreText = font.render("Score: " + str(score), True, white)
        livesText = font.render("Lives: " + str(lives), True, white)

        if not listOfBlocks:
            listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)
        if lives <=0:
            running = gameOver()
            while listOfBlocks:
                listOfBlocks.pop(0)
            lives = 3
            score = 0
            listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    strikerXFac = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    strikerXFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    strikerXFac = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    strikerXFac = 0
                    
        if (collisionChecker(striker.getRect(), ball.getRect())):
            ball.hit()

        for block in listOfBlocks:
            if(collisionChecker(block.getRect(), ball.getRect())):
                ball.hit()
                block.hit()
                if block.getHealth() <= 0:
                    listOfBlocks.pop(listOfBlocks.index(block))
                    score += 5
        striker.update(strikerXFac)
        lifeLost = ball.update()
        if lifeLost:
            lives-=1
            ball.reset()
            print(lives)
        striker.display()
        ball.display()

        for block in listOfBlocks:
            block.display()

        pygame.display.update()
        clock.tick(FPS)

main()
