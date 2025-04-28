import unittest
import pygame

from game_files.game import Game
from game_files.game_loop import GameLoop

test_board = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

cell_size = 50


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.game_1 = Game(test_board, cell_size)

    def test_game_loop(self):
        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_SPACE),
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.KEYDOWN, pygame.K_RIGHT),
            StubEvent(pygame.KEYDOWN, pygame.K_UP),
            StubEvent(pygame.KEYDOWN, pygame.K_DOWN),
            StubEvent(pygame.QUIT, None)
        ]

        game_loop = GameLoop(
            self.game_1,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            cell_size
        )

        game_loop.start()

        self.assertFalse(game_loop._handle_events())
