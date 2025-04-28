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
        matching_users = filter(
            lambda user: user.username == username, self.users)

        matching_users_list = list(matching_users)

        return matching_users_list[0] if len(matching_users_list) > 0 else None

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

    def test_login_correctly(self):
        self.game_service.create_user(
            self.user_u1.username, self.user_u1.password)
        user = self.game_service.login(
            self.user_u1.username, self.user_u1.password)
        self.assertEqual(user.username, self.user_u1.username)
