import pygame


class EventQueue:
    """Tapahtumajonosta vastaava luokka.
    """

    def get(self):
        """Hakee tapahtumat.

        Returns:
            Palauttaa tapahtumat tapahtumajonosta.
        """
        return pygame.event.get()
