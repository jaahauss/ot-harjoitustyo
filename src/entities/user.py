class User:
    """Yksittäistä käyttäjää kuvaava luokka.

    Attributes:
        username: Käyttäjän käyttäjätunnusta kuvaava merkkijono.
        password: Käyttäjän salasanaa kuvaava merkkijono.
    """

    def __init__(self, username, password):
        """Luokan konstruktori.
        """
        self.username = username
        self.password = password
