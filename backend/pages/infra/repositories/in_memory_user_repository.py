from pages.domain.repositories.user_repo import UserRepository
from pages.domain.entities.user import User
from pages.domain.value_objects.email import Email
from pages.domain.value_objects.password import Password
from typing import Optional


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users = {}
        self._current_user_id = None

    def login(self, email: Email, password: Password) -> Optional[User]:
        for user in self._users.values():
            if user.email == email and user.password == password:
                self._current_user_id = user.id
                return user
        return None

    def register(self, user: User) -> User:
        self._users[user.id] = user
        self._current_user_id = user.id
        return user

    def logout(self) -> None:
        self._current_user_id = None

    def get_current_user(self) -> Optional[User]:
        if self._current_user_id is None:
            return None
        return self._users.get(self._current_user_id)

    def set_current_user(self, user: User) -> None:
        self._users[user.id] = user
        self._current_user_id = user.id

