from pages.domain.repositories.book_repo import BookRepository
from pages.domain.entities.book import Book
from typing import List


class GetAllBooksUseCase:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> List[Book]:
        return self.repository.get_all()