import os
import pygame

dirname = os.path.dirname(__file__)


def load_image(filename):
    """Lataa kuvan annetun tiedostonimen perusteella.

        Args:
            filename: Tiedoston nimi

        Returns:
            Palauttaa tiedostonimeä vastaavan kuvan.
        """
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
