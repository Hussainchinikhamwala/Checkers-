import pygame
from constants import WIDTH, HEIGHT
import sys
from board import *
from game import *

WIN  = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("The Utimate Checkers Game!!")

board = Board()
piece = board.get_piece(0,1)
game = ChessGame(WIN)


FPS = 60

def click(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    
    return row,col

def main():

    run = True
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = click(pos)
                game.choose_piece(row, col)
                    
                
        game.update_display()
        
        
    pygame.quit()
    
main()