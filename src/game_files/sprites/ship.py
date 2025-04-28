import pygame
from game_files.load_image import load_image


class Ship(pygame.sprite.Sprite):
    """Laivanosaa kuvaava luokka.

    Perii Sprite-luokan.
    """

    def __init__(self, x=0, y=0):
        """Luokan konstruktori.

        Args:
            x=0: Vapaaehtoinen, oletusarvoltaan 0, x--koordinaattia kuvaava kokonaisluku
            y=0: Vapaaehtoinen, oletusarvoltaan 0, y--koordinaattia kuvaava kokonaisluku
        """
        super().__init__()

        self.image = load_image("ship.png")

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
