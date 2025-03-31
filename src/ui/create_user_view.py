from tkinter import ttk, StringVar, constants
from services.game_service import game_service, UsernameExistsError


class CreateUserView:
    def __init__(self, root, handle_create, handle_login):
        self._root = root
        self._handle_create = handle_create
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0:
            self._error_variable.set("Username is required")
            self._error_label.grid()
            return
        
        if len(password) == 0:
            self._error_variable.set("Password is required")
            self._error_label.grid()
            return

        try:
            game_service.create_user(username, password)
            self._handle_create()
        except UsernameExistsError:
            self._error_variable.set(f"Username {username} already exists")
            self._error_label.grid()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar()
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._error_label.grid(padx=5, pady=5)

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
            text="Create new user",
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._handle_login
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=500)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._error_label.grid_remove()
