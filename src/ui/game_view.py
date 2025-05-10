from tkinter import ttk, constants
from services.game_service import game_service


class GameView:
    """Pelinaloitus-näkymästä vastaava luokka.
    """

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = game_service.get_current_user()
        self._frame = None

        self._start()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _logout_handler(self):
        """Käsittelee uloskirjautumisen.
        """
        game_service.logout()
        self._handle_logout()

    def _start_game(self):
        """Käsittelee pelin aloituksen.
        """
        game_service.start()

    def _start(self):
        """Luo elementit näkymään.
        """
        self._frame = ttk.Frame(master=self._root)

        game_button = ttk.Button(
            master=self._frame,
            text="Start game",
            width=20,
            command=self._start_game
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            width=20,
            command=self._logout_handler
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        game_button.grid(padx=5, pady=5, sticky=constants.E)
        logout_button.grid(padx=5, pady=5, sticky=constants.E)
