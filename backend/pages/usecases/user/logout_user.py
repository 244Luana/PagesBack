from pages.domain.repositories.user_repo import UserRepository

class LogoutUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> None:
        self.repository.logout()