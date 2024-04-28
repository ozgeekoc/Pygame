import pygame , sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
L_W = 15
W_L_W = 15
B_R = 3
B_C = 3
S_SIZE = 200
C_RADIUS = 60
C_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (255,0,0)
BG_COLOR = (20,200,160)
LINE_COLOR = (23,145,135)
circle_color = (239,231,200)
cross_color = (66,66,66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption("TIC TAC TOE")

board = np.zeros((B_R,B_C))

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0,S_SIZE), (WIDTH, S_SIZE), L_W)
    pygame.draw.line(screen, LINE_COLOR, (0, 2*S_SIZE), (WIDTH, 2*S_SIZE), L_W)
    pygame.draw.line(screen, LINE_COLOR, (S_SIZE, 0), (S_SIZE, HEIGHT), L_W)
    pygame.draw.line(screen, LINE_COLOR, (2*S_SIZE, 0), (2*S_SIZE, HEIGHT), L_W)

def draw_figures():
    for row in range(B_R):
        for col in range(B_C):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col*S_SIZE + S_SIZE//2), int(row*S_SIZE + S_SIZE//2)), C_RADIUS, C_WIDTH)
            elif board [row][col] == 2:
                pygame.draw.line(screen, cross_color, (col*S_SIZE + SPACE , row*S_SIZE + S_SIZE - SPACE), (col*S_SIZE + S_SIZE - SPACE , row*S_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, cross_color, (col*S_SIZE + SPACE , row*S_SIZE + SPACE), (col*S_SIZE + S_SIZE - SPACE , row*S_SIZE + S_SIZE - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player 

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(B_R):
        for col in range(B_C):
            if board[row][col]==0:
                return False
    return True
            
def check_win(player):
    for col in range(B_C) :
        if board[0][col]==player and board[1][col]==player and board[2][col]==player :
            draw_vertical_win_line(col,player)
            return True
    for row in range(B_R) :
        if board[row][0]==player and board[row][1]==player and board[row][2]==player :
            draw_horizontal_win_line(row,player)
            return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player :
        draw_asc_diagonal(player)
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player :
        draw_desc_diagonal(player)
        return True
    return False
    
def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, 15), (WIDTH-15, HEIGHT-15), W_L_W)

def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15, 15), W_L_W)

def draw_vertical_win_line(col, player):
    posX = col*S_SIZE + S_SIZE//2
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT-15), W_L_W)

def draw_horizontal_win_line(row, player):
    posY = row*S_SIZE + S_SIZE//2
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, posY), (WIDTH-15 , posY), W_L_W)

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range (B_R):
        for col in range (B_C):
            board[row][col] == 0

draw_lines()
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            c_row = int(mouseY // S_SIZE)
            c_col = int(mouseX // S_SIZE)
            if available_square(c_row, c_col):
                mark_square(c_row, c_col, player)
                if check_win(player):
                    game_over = True
                player= player%2+1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False
    pygame.display.update()
