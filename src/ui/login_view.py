from tkinter import ttk, constants, messagebox
from services.game_service import game_service, InvalidCredentialsError


class LoginView:
    """Kirjautumisnäkymästä vastaava luokka.
    """
    def __init__(self, root, handle_login, handle_create):
        """Luokan konstruktori.

        Args:
            root: Näkymän alustukseen käytettävä TKinter-elementti.
            handle_login: Kirjautumisnäkymääm kutsuttava arvo.
            handle_create: Käyttäjänluomis-näkymään kutsuttava arvo.
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_create = handle_create
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._start()

    def pack(self):
        """Näyttää näkymän.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän.
        """
        self._frame.destroy()

    def _login_handler(self):
        """Käsittelee kirjautumisen.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            game_service.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            messagebox.showerror("Error", "Invalid username or password")

    def _start(self):
        """Luo elementit näkymään.
        """
        self._frame = ttk.Frame(master=self._root)

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            width=20,
            command=self._login_handler
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            width=20,
            command=self._handle_create
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        login_button.grid(padx=5, pady=5, sticky=constants.E)
        create_user_button.grid(padx=5, pady=5, sticky=constants.E)
