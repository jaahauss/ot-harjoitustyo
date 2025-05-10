from game_files.game_start import GameStart

from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class MissingUsernameError(Exception):
    pass


class MissingPasswordError(Exception):
    pass


class GameService:
    """Sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori.

        Args:
            user_repository: Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
        """
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Kirjautuvan käyttäjän käyttäjätunnusta kuvaava merkkijono
            password: Kirjautuvan käyttäjän salasanaa kuvaava merkkijono

        Returns:
            Palauttaa kirjautuneen käyttäjän User-oliona.

        Raises:
            InvalidCredentialsError: Virhe, joka tapahtuu,
                jos käyttäjätunnusta ei ole tai salasana ei täsmää.
        """
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user

    def get_current_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            Palauttaa kirjautuneen käyttäjän User-oliona.
        """
        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan kaikista käyttäjistä.
        """
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa käyttäjän ulos.
        """
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän.

        Args:
           username: Käyttäjätunnusta vastaavan merkkijonon
           password: Salasanaa vastaavan merkkijonon
           login: Vapaaehtoinen, oletusarvoltaan True Boolean-arvo,
               joka kertoo kirjataanko käyttäjä sisään.

        Returns: 
           Palauttaa uuden käyttäjän User-oliona.

        Raises:
           UsernameExistsError: Virhe, joka tapahtuu, jos käyttäjätunnus on jo olemassa.
           MissingUsernameError: Virhe, joka tapahtuu,
           jos käyttäjätunnuksesksi annetaan tyhjä syöte.
           MissingPasswordError: Virhe, joka tapahtuu, jos salasanaksi annetaan tyhjä syöte.
        """
        if len(username) == 0:
            raise MissingUsernameError("Username is required")

        if len(password) == 0:
            raise MissingPasswordError("Password is required")

        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
        return user

    def start(self):
        """Aloittaa pelin.
        """
        game_start = GameStart()
        game_start.start()


game_service = GameService()
