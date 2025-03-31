from tkinter import ttk, constants
from services.game_service import game_service

class GameView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = game_service.get_current_user()
        self._frame = None

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        game_service.logout()
        self._handle_logout()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        logout_button.grid(padx=5, pady=5, sticky=constants.EW)
        
