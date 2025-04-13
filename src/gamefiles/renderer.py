import pygame


class Renderer:
    def __init__(self, screen, game):
        self._screen = screen
        self._game = game

    def render(self):
        self._game.all_sprites.draw(self._screen)

        pygame.display.update()
