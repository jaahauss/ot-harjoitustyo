import pygame


class GameLoop:
    def __init__(self, game, renderer, event_queue, clock, cell_size):
        self._game = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        while True:
            if self._handle_events() is False:
                pygame.quit()
                break

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
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
        self._renderer.render()
