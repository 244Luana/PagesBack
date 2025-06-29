from abc import ABC, abstractmethod
from pages.domain.entities.book import Book

class BookRepository(ABC):
    
    @abstractmethod
    def create(self, book: Book) -> Book:
        pass

    @abstractmethod
    def edit(self, Book) -> Book:
        pass

    @abstractmethod
    def get_all(self) -> list[Book]:
        pass 

    @abstractmethod
    def get_by_id(self, book_id: str) -> Book | None:
        pass


    @abstractmethod
    def delete(self, book_id:str) -> None:
        pass