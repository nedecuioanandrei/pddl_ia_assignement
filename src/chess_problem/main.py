import pygame 
import time

white, black, red = (255, 255, 255), (32, 123, 100), (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Chess visualizer")

game_exit = False 

size = 80

bk_image = pygame.image.load("Chess_ndt60.png")
wk_image = pygame.image.load("Chess_nlt60.png")

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

bk1_pos = Pos(1, 3)
bk2_pos = Pos(3, 3)
wk1_pos = Pos(3, 1)
wk2_pos = Pos(1, 1)

moves = [
    "knight_move w_k_1 n1 n1 n2 n3 (1)",
    "knight_move b_k_1 n1 n3 n3 n2 (1)",
    "knight_move b_k_2 n3 n3 n2 n1 (1)",
    "knight_move b_k_1 n3 n2 n1 n1 (1)",
    "knight_move b_k_2 n2 n1 n1 n3 (1)",
    "knight_move w_k_2 n3 n1 n1 n2 (1)",
    "knight_move w_k_2 n1 n2 n3 n3 (1)",
    "knight_move b_k_2 n1 n3 n3 n2 (1)",
    "knight_move w_k_1 n2 n3 n3 n1 (1)",
    "knight_move b_k_1 n1 n1 n2 n3 (1)",
    "knight_move w_k_1 n3 n1 n1 n2 (1)",
    "knight_move b_k_1 n2 n3 n3 n1 (1)",
    "knight_move w_k_2 n3 n3 n2 n1 (1)",
    "knight_move w_k_1 n1 n2 n3 n3 (1)",
    "knight_move w_k_2 n2 n1 n1 n3 (1)",
    "knight_move b_k_2 n3 n2 n1 n1 (1)",
]    
pos_move = 0


def draw_board():
    gameDisplay.blit(wk_image, (5 + 80 * bk1_pos.x, 5 + 80*bk1_pos.y))     
    gameDisplay.blit(wk_image, (5 + 80 * bk2_pos.x, 5 + 80*bk2_pos.y))

    gameDisplay.blit(bk_image, (5 + 80 * wk1_pos.x, 5 + 80*wk1_pos.y))
    gameDisplay.blit(bk_image, (5 + 80 * wk2_pos.x, 5 + 80*wk2_pos.y))


while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    boardLength = 3
    gameDisplay.fill(white)

    cnt = 1
    for i in range(1, boardLength + 1):
        for z in range(1, boardLength + 1):
            if cnt % 2 == 0:
                pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
            else:
                pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
            cnt += 1

    pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)
    draw_board()
    pygame.display.update()
    if pos_move == len(moves):
        continue 
    move = moves[pos_move]
    pos_move += 1
    move = move.split()
    _, piece, x, y, xx, yy, *_ = move
    
    xx = int(xx[1])
    yy = int(yy[1])

    if piece == "w_k_1":
        wk1_pos = Pos(xx, yy)

    if piece == "w_k_2":
        wk2_pos = Pos(xx, yy)

    if piece == "b_k_1":
        bk1_pos = Pos(xx, yy)

    if piece == "b_k_2":
        bk2_pos = Pos(xx, yy)

    print(pos_move, xx, yy)
    
    time.sleep(2)