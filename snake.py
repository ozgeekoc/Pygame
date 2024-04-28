import pygame , time , random

win_x = 720
win_y = 480 

snake_speed = 15

black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0, 200)

pygame.init()
pygame.display.set_caption("Snake")
game_win = pygame.display.set_mode((win_x, win_y))
fps = pygame.time.Clock()
snake_position = [100,50]
snake_body=[[100,50], 
            [90,50], 
            [80,50], 
            [70,50]
            ]
fruit_pos = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]
fruit_spawn = True

prize_pos = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]
prize_spawn = False

direction = 'RIGHT'
change_to = direction
score = 0
def show_score (choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_win.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont("comicsans", 50)
    over_surface = my_font.render("Your score is " + str(score), True, red)
    game_over_rect = over_surface.get_rect()
    game_over_rect.midtop = (win_x/2, win_y/4)
    game_win.blit(over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"

    if direction == "UP": 
        snake_position[1] -= 10
    if direction == "DOWN": 
        snake_position[1] += 10
    if direction == "LEFT": 
        snake_position[0] -= 10
    if direction == "RIGHT": 
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    if snake_position[0] == fruit_pos[0] and snake_position[1] == fruit_pos[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
    
    if score%5==0:
        prize_pos = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]
        prize_spawn = True
    if prize_spawn :
        pygame.draw.rect(game_win, blue, pygame.Rect(prize_pos[0], prize_pos[1], 10, 10))
    if snake_position[0] == prize_pos[0] and snake_position[1] == prize_pos[0]:
        score += 3
        prize_spawn = False

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (win_x//10))*10, random.randrange(1, (win_y//10))*10]
    fruit_spawn = True
    
        
    game_win.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_win, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_win, white, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))
   
    if snake_position[0]<0 or snake_position[0]>win_x-10:
        game_over()
    if snake_position[1]<0 or snake_position[1]>win_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, "comicsans", 20)
    pygame.display.update()
    fps.tick(snake_speed)
