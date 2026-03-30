from dataclasses import dataclass
from re import fullmatch

from .....config import get_const
from .....shared.utils.misc import Helpers
from ..exceptions import InvalidLengthError, InvalidValueError

const = get_const()


@dataclass(slots=True)
class UserName:
    """class that represents the username of a player"""

    value: str

    def __post_init__(self):
        self.value = Helpers.trim(self.value)
        if not self.value:
            raise InvalidValueError("username is empty")

        length = len(self.value)
        if length < const.USERNAME_MIN_LENGTH or length > const.USERNAME_MAX_LENGTH:
            raise InvalidLengthError(
                f"username must be from {const.USERNAME_MIN_LENGTH} to {const.USERNAME_MAX_LENGTH} characters long"
            )

        if not fullmatch(const.USERNAME_PATTERN, self.value):
            raise InvalidValueError(
                "username must only contain ascii letters, numbers, underscores, dots or dashes"
            )
