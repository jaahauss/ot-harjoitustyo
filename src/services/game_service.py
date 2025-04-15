import pygame
from gamefiles.game import Game
from gamefiles.game_loop import GameLoop
from gamefiles.event_queue import EventQueue
from gamefiles.renderer import Renderer
from gamefiles.clock import Clock

from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class GameService:
    def __init__(
        self,
        user_repository=default_user_repository
    ):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def get_current_user(self):
        return self._user

    def get_users(self):
        return self._user_repository.find_all()

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):
        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user

    def start(self):
        board = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        cell_size = 50

        pygame.display.set_caption("Battleship")
        screen = pygame.display.set_mode((500, 500))
        game = Game(board, cell_size)
        event_queue = EventQueue()
        renderer = Renderer(screen, game)
        clock = Clock()
        game_loop = GameLoop(game, renderer, event_queue, clock, cell_size)
        pygame.init()
        game_loop.start()


game_service = GameService()
