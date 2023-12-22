import pygame
from constants import *
from board import Board

class ChessGame:
    def __init__(self, display_window):
        self.display_window = display_window
        self.selected_piece = None
        self.game_board = Board()
        self.current_player = BROWN
        self.available_moves = {}

    def update_display(self):
        self.game_board.draw(self.display_window)
        self.draw_valid_move_markers(self.available_moves)
        pygame.display.update()

    def determine_winner(self):
        return self.game_board.check_winner()

    def restart_game(self):
        self.selected_piece = None
        self.game_board = Board()
        self.current_player = BROWN
        self.available_moves = {}

    def choose_piece(self, row, col):
        if self.selected_piece:
            successful_move = self.make_move(row, col)
            if not successful_move:
                self.selected_piece = None
                self.choose_piece(row, col)

        piece_at_position = self.game_board.get_piece(row, col)
        if piece_at_position != 0 and piece_at_position.color == self.current_player:
            self.selected_piece = piece_at_position
            self.available_moves = self.game_board.get_valid_moves(piece_at_position)
            return True

        return False

    def make_move(self, row, col):
        target_piece = self.game_board.get_piece(row, col)
        if self.selected_piece and target_piece == 0 and (row, col) in self.available_moves:
            self.game_board.move(self.selected_piece, row, col)
            captured_piece = self.available_moves.get((row, col))
            if captured_piece:
                self.game_board.remove(captured_piece)
            self.switch_player_turn()

        return True

    def draw_valid_move_markers(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.display_window, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def switch_player_turn(self):
        self.available_moves = {}
        if self.current_player == WHITE:
            self.current_player = BROWN
            
        else:
            self.current_player = WHITE