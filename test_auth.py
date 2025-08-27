import pytest

class InvalidCredentials(Exception):
    """Raised when username or password is invalid."""


class AuthService:
    def __init__(self):
        self._users = {"alice": "password123", "bob": "qwerty"}

    def login(self, username: str, password: str) -> bool:
        if username not in self._users:
            raise InvalidCredentials("Unknown user")

        if self._users[username] != password:
            raise InvalidCredentials("Wrong password")

        return True


# ---------------- CLI part with input ----------------
def main():
    service = AuthService()
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        if service.login(username, password):
            print("Login successful ✅")
    except InvalidCredentials as e:
        print(f"Login failed ❌: {e}")


# ------------------- TESTS -------------------
@pytest.fixture
def auth_service():
    return AuthService()


def test_login_success(auth_service):
    assert auth_service.login("alice", "password123") is True


def test_login_wrong_password(auth_service):
    with pytest.raises(InvalidCredentials):
        auth_service.login("bob", "wrong")


def test_login_unknown_user(auth_service):
    with pytest.raises(InvalidCredentials):
        auth_service.login("charlie", "abc")


def test_login_with_mocked_input(monkeypatch, capsys):
    # simulate user typing "alice" and "password123"
    monkeypatch.setattr("builtins.input", lambda prompt: "alice" if "username" in prompt else "password123")
    
    main()

    captured = capsys.readouterr()
    assert "Login successful" in captured.out