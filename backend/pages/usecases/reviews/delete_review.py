from pages.domain.repositories.review_repo import ReviewRepository


class DeleteReviewUseCase:
    def __init__(self, repository: ReviewRepository):
        self.repository = repository

    def execute(self, review_id: str) -> None:
        self.repository.delete_review(review_id)