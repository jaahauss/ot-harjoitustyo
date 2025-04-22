import pygame


class Renderer:
    def __init__(self, screen, game):
        self._screen = screen
        self._game = game
        self._fontti = pygame.font.SysFont("Arial", 24)

    def render(self):
        self._screen.fill((255, 255, 255))
        self._game.all_sprites.draw(self._screen)

        text_1 = self._fontti.render(
            f"Shots: {self._game.shots}", True, (255, 0, 0))
        text_2 = self._fontti.render(
            f"Shots to target: {self._game.shots_to_target}", True, (255, 0, 0))
        self._screen.blit(text_1, (0, 510))
        self._screen.blit(text_2, (0, 530))

        pygame.display.update()
