import random
import pygame
from gamefiles.sprites.sea import Sea
from gamefiles.sprites.ship import Ship
from gamefiles.sprites.highlight import Highlight


class Game:
    def __init__(self, board, cell_size):
        self.cell_size = cell_size
        self.ships = pygame.sprite.Group()
        self.seas = pygame.sprite.Group()
        self.highlight = None
        self.all_sprites = pygame.sprite.Group()

        new_board = self._add_ships(board)
        self._initialize_sprites(new_board)

    def _initialize_sprites(self, board):
        height = len(board)
        width = len(board[0])
        for y in range(height):
            for x in range(width):
                cell = board[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.seas.add(Sea(normalized_x, normalized_y))
                elif cell == 1:
                    self.ships.add(Ship(normalized_x, normalized_y))
                elif cell == 2:
                    self.highlight = Highlight(normalized_x, normalized_y)
                    self.seas.add(Sea(normalized_x, normalized_y))
                elif cell == 3:
                    self.highlight = Highlight(normalized_x, normalized_y)
                    self.ships.add(Ship(normalized_x, normalized_y))

        self.all_sprites.add(
            self.seas,
            self.ships,
            self.highlight
        )

    def move_highlight(self, dx=0, dy=0):
        self.highlight.rect.move_ip(dx, dy)

    def _add_ships(self, board):
        ship_lengths = [5, 4, 3, 2, 1]
        for i in range(5):
            start_y, start_x, direction = self._find_start(ship_lengths[i])
            if direction == "down":
                for n in range(ship_lengths[i]):
                    if board[start_y+n][start_x] == 2:
                        board[start_y+n][start_x] = 3
                    else:
                        board[start_y+n][start_x] = 1
            else:
                for n in range(ship_lengths[i]):
                    if board[start_y][start_x+n] == 2:
                        board[start_y][start_x+n] = 3
                    else:
                        board[start_y][start_x+n] = 1
        return board

    def _find_start(self, length):
        direction = random.randint(1, 2)
        if direction == 1:
            return (random.randint(0, 9-length), random.randint(0, 9), "down")
        return (random.randint(0, 9), random.randint(0, 9-length), "right")
