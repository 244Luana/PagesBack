from abc import ABC, abstractmethod
from pages.domain.entities.review import Review

class ReviewRepository(ABC):
    @abstractmethod
    def create(self, review: Review) -> Review:
        pass

    @abstractmethod
    def get_by_id(self, review_id: str) -> Review | None:
        pass

    @abstractmethod
    def update(self, review: Review) -> Review:
        pass

    @abstractmethod
    def delete(self, review_id: str) -> None:
        pass

    @abstractmethod
    def get_reviews_by_book(self, book_id: str) -> list[Review]:
        pass

    @abstractmethod
    def get_reviews_by_user(self, user_id: str) -> list[Review]:
        pass
