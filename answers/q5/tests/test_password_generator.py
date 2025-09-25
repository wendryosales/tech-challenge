from app.core.utils.passwords import PasswordGenerator


def test_password_generator_length():
    pwd = PasswordGenerator.generate(16)
    assert len(pwd) >= 16


def test_password_generator_varies():
    p1 = PasswordGenerator.generate(16)
    p2 = PasswordGenerator.generate(16)
    assert p1 != p2
