from pages.domain.value_objects.email import Email
from pages.domain.value_objects.password import Password
from pages.domain.entities.user import User
from pages.domain.repositories.user_repo import UserRepository
from typing import Optional

class LoginUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: Email, password: Password) -> Optional[User]:
        return self.repository.login(email, password)