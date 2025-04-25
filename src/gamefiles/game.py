import random
import pygame
from gamefiles.sprites.sea import Sea
from gamefiles.sprites.ship import Ship
from gamefiles.sprites.hit import Hit
from gamefiles.sprites.miss import Miss
from gamefiles.sprites.shipwreck import Shipwreck
from gamefiles.sprites.highlight import Highlight


class Game:
    def __init__(self, board, cell_size):
        self.cell_size = cell_size
        self.ships = pygame.sprite.Group()
        self.seas = pygame.sprite.Group()
        self.hits = pygame.sprite.Group()
        self.misses = pygame.sprite.Group()
        self.shipwrecks = pygame.sprite.Group()
        self.highlight = None
        self.all_sprites = pygame.sprite.Group()
        self.shots = 0
        self.shots_to_target = 0
        self.sunken_ships = 0

        target_x = 0
        target_y = 0

        self.board = self._add_ships(board)
        self._initialize_sprites(target_x, target_y)

    def _initialize_sprites(self, target_x, target_y):
        height = len(self.board)
        width = len(self.board[0])
        self.highlight = Highlight(target_x, target_y)
        for y in range(height):
            for x in range(width):
                cell = self.board[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.seas.add(Sea(normalized_x, normalized_y))
                elif cell == 1:
                    self.ships.add(Ship(normalized_x, normalized_y))
                elif cell == 2:
                    self.ships.add(Hit(normalized_x, normalized_y))
                elif cell == 3:
                    self.ships.add(Miss(normalized_x, normalized_y))
                elif cell == 4:
                    self.ships.add(Shipwreck(normalized_x, normalized_y))

        self.all_sprites.add(
            self.seas,
            self.ships,
            self.hits,
            self.misses,
            self.shipwrecks,
            self.highlight
        )

    def move_highlight(self, dx=0, dy=0):
        if self._check_collision(dx, dy):
            self.highlight.rect.move_ip(dx, dy)

    def _check_collision(self, dx, dy):
        if dx < 0 and self.highlight.rect.x <= 0:
            return False
        if dx > 0 and self.highlight.rect.x >= 450:
            return False
        if dy < 0 and self.highlight.rect.y <= 0:
            return False
        if dy > 0 and self.highlight.rect.y >= 450:
            return False
        return True

    def _add_ships(self, board):
        ship_lengths = [5, 4, 3, 2, 2]
        self.added_ships = []
        for i in range(5):
            valid_position = False
            while not valid_position:
                coordinate_1 = random.randint(0, 9-ship_lengths[i])
                coordinate_2 = random.randint(0, 9)
                direction = random.choice(["down", "right"])
                if direction == "down":
                    valid_position = self._check_valid_position(
                        ship_lengths[i], coordinate_1, coordinate_2, board)
                    if valid_position:
                        ship = []
                        for n in range(ship_lengths[i]):
                            board[coordinate_1+n][coordinate_2] = 1
                            ship.append((coordinate_1+n, coordinate_2))
                        self.added_ships.append(ship)
                else:
                    valid_position = self._check_valid_position(
                        ship_lengths[i], coordinate_2, coordinate_1, board)
                    if valid_position:
                        ship = []
                        for n in range(ship_lengths[i]):
                            board[coordinate_2][coordinate_1+n] = 1
                            ship.append((coordinate_2, coordinate_1+n))
                        self.added_ships.append(ship)
        return board

    def _check_valid_position(self, length, c_1, c_2, board):
        for n in range(c_1-1, c_1+length+1):
            for m in range(c_2-1, c_2+length+1):
                if m < 0 or n < 0 or m > 9 or n > 9:
                    continue
                if board[n][m] == 1:
                    return False
        return True

    def shoot(self):
        x = self.highlight.rect.x
        y = self.highlight.rect.y
        shot_x = x // self.cell_size
        shot_y = y // self.cell_size
        cell = self.board[shot_y][shot_x]
        if cell == 1:
            self.shots_to_target += 1
            self.shots += 1
            self.board[shot_y][shot_x] = 2
            if self._check_sunken(shot_y, shot_x):
                self.sunken_ships += 1
            self._initialize_sprites(x, y)
        elif cell in (2, 3):
            pass
        else:
            self.shots += 1
            self.board[shot_y][shot_x] = 3
            self._initialize_sprites(x, y)

    def _check_sunken(self, y, x):
        for ship in self.added_ships:
            checker_1 = 0
            checker_2 = 0
            for coordinate in ship:
                if self.board[coordinate[0]][coordinate[1]] == 2:
                    checker_1 += 1
                if coordinate[0] == y and coordinate[1] == x:
                    checker_2 = 1
            if checker_1 == len(ship) and checker_2 == 1:
                for coordinate in ship:
                    self.board[coordinate[0]][coordinate[1]] = 4
                return True
        return False

    def check_game_over(self):
        if self.sunken_ships == 5:
            return True
        return False
