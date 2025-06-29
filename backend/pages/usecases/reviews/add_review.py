from pages.domain.entities.review import Review
from pages.domain.repositories.review_repo import ReviewRepository


class AddReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    def execute(self, review: Review) -> Review:
        return self.repository.add_review(review)