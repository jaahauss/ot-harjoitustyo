from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Käyttäjiin liittyvästä tietokannasta vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self._connection = connection

    def find_all(self):
        """Etsii kaikki käyttäjät.

        Returns:
            Palauttaa listan User-olioita.
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def find_by_username(self, username):
        """Etsii käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Käyttäjätunnus, jonka perusteella etsitään käyttäjää.

        Returns:
            Palauttaa käyttäjätunnusta vastaavan User-olion, jos käyttäjä on tietokannassa.
            Palauttaa None, jos käyttäjä ei ole tietokannassa.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return User(row["username"], row["password"]) if row else None

    def create(self, user):
        """Luo uuden käyttäjän lisäämällä tietokantaan.

        Args:
            user: Uusi käyttäjä User-oliona.

        Returns:
            Tallennettu käyttjä User-oliona.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """
        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
