from pages.domain.entities.user import User
from pages.domain.repositories.user_repo import UserRepository

class RegisterUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user: User) -> User:
        return self.repository.register(user)