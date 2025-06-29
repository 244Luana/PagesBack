import pytest
import uuid
from pages.domain.entities.user import User
from pages.domain.value_objects.email import Email
from pages.domain.value_objects.password import Password
from pages.infra.repositories.in_memory_user_repository import InMemoryUserRepository
from pages.usecases.user.register_user import RegisterUserUseCase
from pages.usecases.user.login_user import LoginUserUseCase
from pages.usecases.user.logout_user import LogoutUserUseCase
from pages.usecases.user.get_current_user import GetCurrentUserUseCase
from pages.usecases.user.set_current_user import SetCurrentUserUseCase

@pytest.fixture
def user_repository():
    return InMemoryUserRepository()

@pytest.fixture
def sample_user():
    return User(
        id=str(uuid.uuid4()),
        name="Test User",
        email=Email("test@example.com"),
        password=Password("SecurePass123"),
        role="user"
    )

def test_register_user(user_repository, sample_user):
    usecase = RegisterUserUseCase(user_repository)
    result = usecase.execute(sample_user)

    assert result == sample_user
    assert user_repository.get_current_user() == sample_user

def test_login_user_success(user_repository, sample_user):
    user_repository.register(sample_user) # Register the user first

    usecase = LoginUserUseCase(user_repository)
    result = usecase.execute(sample_user.email, sample_user.password)

    assert result == sample_user
    assert user_repository.get_current_user() == sample_user

def test_login_user_failure_wrong_credentials(user_repository, sample_user):
    user_repository.register(sample_user)
    wrong_email = Email("wrong@example.com")
    wrong_password = Password("WrongPass123")

    usecase = LoginUserUseCase(user_repository)
    result = usecase.execute(wrong_email, wrong_password)

    assert result is None
    assert user_repository.get_current_user() is None

def test_logout_user(user_repository, sample_user):
    user_repository.register(sample_user)
    user_repository.login(sample_user.email, sample_user.password)

    usecase = LogoutUserUseCase(user_repository)
    usecase.execute()

    assert user_repository.get_current_user() is None

def test_get_current_user(user_repository, sample_user):
    user_repository.register(sample_user)

    usecase = GetCurrentUserUseCase(user_repository)
    result = usecase.execute()

    assert result == sample_user

def test_get_current_user_no_user_logged_in(user_repository):
    usecase = GetCurrentUserUseCase(user_repository)
    result = usecase.execute()
    assert result is None

def test_set_current_user(user_repository, sample_user):
    usecase = SetCurrentUserUseCase(user_repository)
    usecase.execute(sample_user)

    assert user_repository.get_current_user() == sample_user


