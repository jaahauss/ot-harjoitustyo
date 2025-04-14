from tkinter import ttk, messagebox, constants
from gamefiles.game_service import game_service, UsernameExistsError


class CreateUserView:
    def __init__(self, root, handle_create, handle_login):
        self._root = root
        self._handle_create = handle_create
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0:
            messagebox.showerror("Error", "Username is required")
            return

        if len(password) == 0:
            messagebox.showerror("Error", "Password is required")
            return

        try:
            game_service.create_user(username, password)
            self._handle_create()
        except UsernameExistsError:
            messagebox.showerror(
                "Error", f"Username {username} already exists")

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create",
            width=20,
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Back to login page",
            width=20,
            command=self._handle_login
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        create_user_button.grid(padx=5, pady=5, sticky=constants.E)
        login_button.grid(padx=5, pady=5, sticky=constants.E)
