import pytest
from rest_framework.test import APIClient
from flashcards.models import User, FlashcardSet, Flashcard

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def _create_user(username, is_admin=False):
        return User.objects.create(username=username, is_admin=is_admin)
    return _create_user

@pytest.fixture
def create_flashcard_set(create_user):
    def _create_flashcard_set(name, user):
        return FlashcardSet.objects.create(name=name)
    return _create_flashcard_set

@pytest.fixture
def create_flashcard(create_flashcard_set):
    def _create_flashcard(question, answer, difficulty, flashcard_set):
        return Flashcard.objects.create(
            question=question,
            answer=answer,
            difficulty=difficulty,
            set=flashcard_set,
        )
    return _create_flashcard

def test_user_creation(api_client, create_user):
    user = create_user(username="test_user")
    response = api_client.get("/api/users/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["username"] == "test_user"

def test_flashcard_set_creation(api_client, create_user, create_flashcard_set):
    user = create_user(username="test_user")
    flashcard_set = create_flashcard_set(name="Test Set", user=user)
    response = api_client.get("/api/sets/")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Test Set"
