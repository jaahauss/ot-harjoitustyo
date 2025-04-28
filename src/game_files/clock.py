import pygame


class Clock:
    """Pelikellosta vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori.
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Kutsuu Clock-luokan tick-metodia.
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Hakee ajan pygamen käynnistämisestä.

        Returns:
            Palauttaa ajan siitä, kun kutsuttiin pygame.init().
        """
        return pygame.time.get_ticks()
