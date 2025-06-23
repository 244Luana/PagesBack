from abc import ABC, abstractmethod
from site.domain.entities.book import Book

class BookRepository(ABC):
    
    @abstractmethod
    def create(self, id: str, title: str, author: str, genre: str) -> Book:
        pass

    @abstractmethod
    def edit(self, Book) -> Book:
        pass

    @abstractmethod
    def get_all(self) -> list[Book]:
        pass 

    @abstractmethod
    def delete(self, book_id:str) -> None:
        pass