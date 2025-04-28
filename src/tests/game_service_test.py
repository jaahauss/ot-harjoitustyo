import unittest
from entities.user import User
from services.game_service import (
    GameService,
    InvalidCredentialsError,
    UsernameExistsError
)


class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def find_all(self):
        return self.users

    def find_by_username(self, username):
        user_list = list(
            filter(lambda user: user.username == username, self.users))

        return user_list[0] if len(user_list) > 0 else None

    def create(self, user):
        self.users.append(user)

        return user

    def delete_all(self):
        self.users = []


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.game_service = GameService(FakeUserRepository())

        self.user_u1 = User('u1', 'pw1')

    def create_user(self, user):
        self.game_service.create_user(user.username, user.password)

    def test_create_user(self):
        self.game_service.create_user(
            self.user_u1.username, self.user_u1.password)
        users = self.game_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_u1.username)
        self.assertEqual(users[0].password, self.user_u1.password)

        self.assertRaises(UsernameExistsError, lambda: self.game_service.create_user(
            self.user_u1.username, 'password'))

    def test_login(self):
        self.game_service.create_user(
            self.user_u1.username, self.user_u1.password)
        user = self.game_service.login(
            self.user_u1.username, self.user_u1.password)

        self.assertEqual(user.username, self.user_u1.username)

        self.assertRaises(InvalidCredentialsError,
                          lambda: self.game_service.login(user.username, 'wrong'))
