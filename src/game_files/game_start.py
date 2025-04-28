import pygame
from game_files.game import Game
from game_files.game_loop import GameLoop
from game_files.event_queue import EventQueue
from game_files.renderer import Renderer
from game_files.clock import Clock


class GameStart:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.cell_size = 50

    def start(self):
        pygame.init()
        game = Game(self.board, self.cell_size)
        event_queue = EventQueue()
        renderer = Renderer(game)
        clock = Clock()
        game_loop = GameLoop(game, renderer, event_queue,
                             clock, self.cell_size)
        game_loop.start()
