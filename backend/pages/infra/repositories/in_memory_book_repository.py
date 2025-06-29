from pages.domain.repositories.book_repo import BookRepository
from pages.domain.entities.book import Book
from typing import List, Optional

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self._posts = {}

    def get_all(self) -> List[Book]:
        return list(self._posts.values())

    def get_by_id(self, book_id: str) -> Optional[Book]:
        return self._posts.get(book_id)

    def create(self, book: Book) -> Book:
        self._posts[book.id] = book
        return book

    def update(self, book: Book) -> Optional[Book]:
        if book.id in self._posts:
            self._posts[book.id] = book
            return book
        return None

    def delete(self, book_id: str) -> None:
        self._posts.pop(book_id, None)