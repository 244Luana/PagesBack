from pages.domain.entities.book import Book
from pages.domain.repositories.book_repo import BookRepository
from typing import Optional


class UpdateBookUseCase:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book: Book) -> Optional[Book]:
        return self.repository.update(book)