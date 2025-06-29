from pages.domain.entities.book import Book
from pages.domain.repositories.book_repo import BookRepository


class CreatePostUseCase:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book: Book) -> Book:
        return self.repository.create(book)