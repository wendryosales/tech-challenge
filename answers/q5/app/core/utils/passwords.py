from math import ceil
from secrets import token_urlsafe


class PasswordGenerator:
    @staticmethod
    def generate(target_length: int = 12) -> str:
        nbytes = max(8, ceil(target_length * 3 / 4))
        return token_urlsafe(nbytes)
