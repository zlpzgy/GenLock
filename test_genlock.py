import pytest
from test_project import generate_password, is_password_strong, obscure_password

def test_generate_password():
    password = generate_password(12)
    assert isinstance(password, str)
    assert len(password) == 12

def test_is_password_strong():
    assert is_password_strong("abc") == "Weak"
    assert is_password_strong("abc12345") == "Moderate"
    assert is_password_strong("aB1@xY#z9!") == "Strong"

def test_obscure_password():
    assert obscure_password("abcd") == "****"
    assert obscure_password("abcdefgh") == "ab****gh"
