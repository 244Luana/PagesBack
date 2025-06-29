from pages.domain.repositories.book_repo import BookRepository


class DeleteBookUseCase:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: str) -> None:
        self.repository.delete(book_id)