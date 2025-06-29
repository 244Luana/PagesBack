import pytest
from pages.domain.entities.user import User
from pages.domain.entities.book import Book
from pages.domain.entities.review import Review
from pages.domain.value_objects.email import Email
from pages.domain.value_objects.password import Password

def test_create_user():
    email = Email("user@example.com")
    pwd = Password("Secret123")
    user = User("1", "User Name", email, pwd, "user")
    assert user.name == "User Name"
    assert user.email == email
    assert user.password == pwd
    assert user.role == "user"

def test_invalid_user_role():
    with pytest.raises(ValueError, match="O perfil deve ser 'admin' ou 'user'"):
        User("1", "User Name", Email("user@example.com"), Password("Secret123"), "invalid_role")

def test_create_book():
    book = Book("book1", "Title Example", "Author Name", "Fiction", "poster_url.jpg")
    assert book.title == "Title Example"
    assert book.author == "Author Name"
    assert book.genre == "Fiction"
    assert book.poster == "poster_url.jpg"

def test_create_review():
    review = Review("review1", "Book Title", "Book Author", "5", "Great book!")
    assert review.book_title == "Book Title"
    assert review.rate == "5"
    assert review.review == "Great book!"