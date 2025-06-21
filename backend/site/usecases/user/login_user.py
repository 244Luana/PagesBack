from site.domain.value_objects.email import Email
from site.domain.value_objects.password import Password
from site.domain.entities.user import User
from site.domain.repositories.user_repo import UserRepository
from typing import Optional

class LoginUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: Email, password: Password) -> Optional[User]:
        return self.repository.login(email, password)