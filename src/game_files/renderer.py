import pygame


class Renderer:
    """Pelin näkymien piirtämisestä vastaava luokka.
    """

    def __init__(self, game):
        """Luokan konstruktori, joka määrittelee näytön ja käytetyt fontit.

        Args:
            game: Game-luokan olio
        """
        self._screen = pygame.display.set_mode((500, 580))
        self._game = game
        self._fontti = pygame.font.SysFont("Arial", 24)
        self._fontti_big = pygame.font.SysFont("Arial", 48)

    def render(self):
        """Piirtää näkymän.

        Returns:
            Palauttaa False, jos peli on päättynyt.
            Muussa tapauksessa palauttaa True.
        """
        pygame.display.set_caption("Battleship")
        self._screen.fill((0, 0, 0))
        if self._game.check_game_over():
            text_1 = self._fontti_big.render("GAME OVER", True, (0, 128, 0))
            text_2 = self._fontti.render(
                f"You completed the game in {self._game.shots} shots", True, (255, 255, 0))
            self._screen.blit(text_1, (0, 250))
            self._screen.blit(text_2, (0, 300))
            pygame.display.update()
            return False

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
