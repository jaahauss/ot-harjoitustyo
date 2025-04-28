import pygame


class GameLoop:
    """Pelisilmukasta vastaava luokka.
    """

    def __init__(self, game, renderer, event_queue, clock, cell_size):
        """Luokan konstruktori.

        Args:
            game: Game-olio
            renderer: Renderer-olio
            event_queue: EventQueue-olio
            clock: Clock-olio
            cell_size: Solun kokoa kuvaava kokonaisluku
        """
        self._game = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        """Aloittaa pelisilmukan.
        """
        while True:
            if self._handle_events() is False:
                pygame.quit()
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        """Käsittelee tapahtumat.

        Returns:
            Palauttaa False, jos tapahtumatyyppi on quit.
        """
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._game.shoot()
                if event.key == pygame.K_LEFT:
                    self._game.move_highlight(dx=-self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self._game.move_highlight(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self._game.move_highlight(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self._game.move_highlight(dy=self._cell_size)
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        """Piirtää pelinäkymän kutsumalla Renderer-olion vastaavaa luokkaa.
        """
        self._renderer.render()
