import pygame


class Renderer:
    def __init__(self, screen, game):
        self._screen = screen
        self._game = game
        self._fontti = pygame.font.SysFont("Arial", 24)
        self._fontti_big = pygame.font.SysFont("Arial", 48)

    def render(self):
        if self._game.check_game_over():
            self._screen.fill((0, 0, 0))
            text_1 = self._fontti_big.render("GAME OVER", True, (0, 128, 0))
            text_2 = self._fontti.render(
                f"You completed the game in {self._game.shots} shots", True, (255, 255, 0))
            self._screen.blit(text_1, (0, 250))
            self._screen.blit(text_2, (0, 300))
            pygame.display.update()
            return False

        self._screen.fill((255, 255, 255))
        self._game.all_sprites.draw(self._screen)
        text_1 = self._fontti.render(
            f"Shots: {self._game.shots}", True, (255, 0, 0))
        text_2 = self._fontti.render(
            f"Shots to target: {self._game.shots_to_target} out of 16", True, (255, 255, 0))
        text_3 = self._fontti.render(
            f"Sunken ships: {self._game.sunken_ships} out of 5", True, (0, 128, 0))
        self._screen.blit(text_1, (0, 510))
        self._screen.blit(text_2, (0, 530))
        self._screen.blit(text_3, (0, 550))

        pygame.display.update()
        return True
