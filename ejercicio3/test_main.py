import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.mark.parametrize("palindrome_word", ["kayak", "rotator"])
def test_is_palindrome_endpoint_returns_true(palindrome_word: str):
    response = client.get(f"/?input={palindrome_word}")
    assert response.status_code == 200
    assert response.json() == {"palindrome": True}


@pytest.mark.parametrize("non_palindrome_word", ["Hello", "World"])
def test_is_palindrome_endpoint_returns_false(non_palindrome_word: str):
    response = client.get(f"/?input={non_palindrome_word}")
    assert response.status_code == 200
    assert response.json() == {"palindrome": False}
