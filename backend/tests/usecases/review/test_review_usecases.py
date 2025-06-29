import pytest
import uuid
from pages.domain.entities.review import Review
from pages.infra.repositories.in_memory_review_repository import InMemoryReviewRepository # Corrected class name
from pages.usecases.reviews.add_review import AddReviewUseCase
from pages.usecases.reviews.delete_review import DeleteReviewUseCase
from pages.usecases.reviews.get_reviews_by_book import GetReviewsByBookUseCase
from pages.usecases.reviews.get_reviews_by_user import GetReviewsByUserUseCase

@pytest.fixture
def review_repository():
    return InMemoryReviewRepository()

@pytest.fixture
def sample_review():
    return Review(
        id=str(uuid.uuid4()),
        book_title="Sample Book Title",
        book_author="Sample Author",
        rate="5",
        review="This is a sample review."
    )

def test_add_review(review_repository, sample_review):
    usecase = AddReviewUseCase(review_repository)
    result = usecase.execute(sample_review)

    assert result == sample_review
    assert review_repository._reviews[sample_review.id] == sample_review # Corrected attribute name

def test_get_reviews_by_book(review_repository):
    review1 = Review(id=str(uuid.uuid4()), book_title="Book A", book_author="Author X", rate="4", review="Good.")
    review2 = Review(id=str(uuid.uuid4()), book_title="Book A", book_author="Author Y", rate="5", review="Excellent.")
    review3 = Review(id=str(uuid.uuid4()), book_title="Book B", book_author="Author Z", rate="3", review="Okay.")

    review_repository.add_comment(review1)
    review_repository.add_comment(review2)
    review_repository.add_comment(review3)

    usecase = GetReviewsByBookUseCase(review_repository)
    result = usecase.execute("Book A")

    assert len(result) == 2
    assert review1 in result
    assert review2 in result
    assert review3 not in result

def test_get_reviews_by_book_empty(review_repository):
    usecase = GetReviewsByBookUseCase(review_repository)
    result = usecase.execute("Non Existent Book")

    assert result == []

def test_get_reviews_by_user(review_repository):
    review1 = Review(id=str(uuid.uuid4()), book_title="Book C", book_author="Author P", rate="4", review="Nice.")
    review2 = Review(id=str(uuid.uuid4()), book_title="Book D", book_author="Author P", rate="5", review="Very good.")
    review3 = Review(id=str(uuid.uuid4()), book_title="Book E", book_author="Author Q", rate="3", review="Average.")

    review_repository.add_comment(review1)
    review_repository.add_comment(review2)
    review_repository.add_comment(review3)

    usecase = GetReviewsByUserUseCase(review_repository)
    result = usecase.execute("Author P")

    assert len(result) == 2
    assert review1 in result
    assert review2 in result
    assert review3 not in result

def test_get_reviews_by_user_empty(review_repository):
    usecase = GetReviewsByUserUseCase(review_repository)
    result = usecase.execute("Non Existent Author")

    assert result == []

def test_delete_review(review_repository, sample_review):
    review_repository.add_comment(sample_review)

    usecase = DeleteReviewUseCase(review_repository)
    usecase.execute(sample_review.id)

    assert sample_review.id not in review_repository._reviews # Corrected attribute name

def test_delete_review_not_found(review_repository):
    usecase = DeleteReviewUseCase(review_repository)

    # Just ensure it doesn\'t raise an error
    usecase.execute("id-invalido")


