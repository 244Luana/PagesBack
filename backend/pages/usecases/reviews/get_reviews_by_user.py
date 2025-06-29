from pages.domain.repositories.review_repo import ReviewRepository
from pages.domain.entities.review import Review
from typing import List


class GetReviewsByUserUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    def execute(self, user_id: str) -> List[Review]:
        return self.repository.get_reviews_by_user(user_id)