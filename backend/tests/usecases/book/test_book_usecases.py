import pytest
import uuid
from pages.domain.entities.book import Book
from pages.infra.repositories.in_memory_book_repository import InMemoryBookRepository
from pages.usecases.book.create_book import CreatePostUseCase # Note: The class name is CreatePostUseCase in the provided code
from pages.usecases.book.delete_book import DeleteBookUseCase
from pages.usecases.book.get_all_books import GetAllBooksUseCase
from pages.usecases.book.get_book_by_id import GetBookByIdUseCase
from pages.usecases.book.update_book import UpdateBookUseCase

@pytest.fixture
def book_repository():
    return InMemoryBookRepository()

@pytest.fixture
def sample_book():
    return Book(
        id=str(uuid.uuid4()),
        title="Sample Book Title",
        author="Sample Author",
        genre="Fiction",
        poster="http://example.com/poster.jpg"
    )

def test_create_book(book_repository, sample_book):
    usecase = CreatePostUseCase(book_repository) # Using CreatePostUseCase as per provided code
    result = usecase.execute(sample_book)

    assert result == sample_book
    assert book_repository.get_by_id(sample_book.id) == sample_book

def test_get_all_books(book_repository, sample_book):
    book_repository.create(sample_book)
    book2 = Book(
        id=str(uuid.uuid4()),
        title="Another Book",
        author="Another Author",
        genre="Mystery",
        poster="http://example.com/another_poster.jpg"
    )
    book_repository.create(book2)

    usecase = GetAllBooksUseCase(book_repository)
    result = usecase.execute()

    assert len(result) == 2
    assert sample_book in result
    assert book2 in result

def test_get_book_by_id(book_repository, sample_book):
    book_repository.create(sample_book)

    usecase = GetBookByIdUseCase(book_repository)
    result = usecase.execute(sample_book.id)

    assert result == sample_book

def test_get_book_by_id_not_found(book_repository):
    usecase = GetBookByIdUseCase(book_repository)
    result = usecase.execute("id-invalido")

    assert result is None

def test_update_book(book_repository, sample_book):
    book_repository.create(sample_book)

    updated_book = Book(
        id=sample_book.id,
        title="Updated Title",
        author="Updated Author",
        genre="Science Fiction",
        poster="http://example.com/updated_poster.jpg"
    )

    usecase = UpdateBookUseCase(book_repository)
    result = usecase.execute(updated_book)

    assert result == updated_book
    assert book_repository.get_by_id(sample_book.id) == updated_book

def test_update_book_not_found(book_repository, sample_book):
    usecase = UpdateBookUseCase(book_repository)
    result = usecase.execute(sample_book)

    assert result is None

def test_delete_book(book_repository, sample_book):
    book_repository.create(sample_book)

    usecase = DeleteBookUseCase(book_repository)
    usecase.execute(sample_book.id)

    assert book_repository.get_by_id(sample_book.id) is None
    
def test_delete_book_not_found(book_repository):
    usecase = DeleteBookUseCase(book_repository)

    # Apenas garantir que não levanta exceção
    usecase.execute("id-invalido")


