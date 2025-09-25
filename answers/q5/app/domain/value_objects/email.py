from email_validator import EmailNotValidError, validate_email


class Email:
    def __init__(self, value: str) -> None:
        try:
            info = validate_email(value, check_deliverability=False)
        except EmailNotValidError as e:
            raise ValueError(f"invalid email: {e}")
        self._value = info.normalized

    def __str__(self) -> str:
        return self._value
