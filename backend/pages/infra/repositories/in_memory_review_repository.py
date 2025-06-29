from pages.domain.repositories.review_repo import ReviewRepository
from pages.domain.entities.review import Review
from typing import List


class InMemoryReviweRepository(ReviewRepository):
    def __init__(self):
        self._reviews = {}

    def get_reviews_by_book(self, book_id: str) -> List[Review]:
        return [c for c in self._reviews.values() if c.book_id == book_id]

    def get_reviews_by_user(self, user_id: str) -> List[Review]:
        return [c for c in self._reviews.values() if c.user_id == user_id]

    def add_review(self, review: Review) -> Review:
        self._reviews[review.id] = review
        return review

    def delete_review(self, review_id: str) -> None:
        self._reviews.pop(review_id, None)