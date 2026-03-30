from dataclasses import dataclass
from re import fullmatch

from .....config import get_const
from .....shared.utils.misc import Helpers
from ..exceptions import InvalidLengthError, InvalidValueError

const = get_const()


@dataclass(slots=True)
class Email:
    """class that represents the email address of a player"""

    value: str

    def __post_init__(self):
        self.value = Helpers.trim(self.value)
        if not self.value:
            raise InvalidValueError("email is empty")

        length = len(self.value)
        if length < const.EMAIL_MIN_LENGTH or length > const.EMAIL_MAX_LENGTH:
            raise InvalidLengthError(
                f"email must be from {const.EMAIL_MIN_LENGTH} to {const.EMAIL_MAX_LENGTH} characters long"
            )

        if not fullmatch(const.EMAIL_PATTERN, self.value):
            raise InvalidValueError("email is invalid")

    @property
    def provider(self) -> str:
        """get the email provider, ex. gmail.com, mail.ru etc."""
        return self.value.split("@")[1]
