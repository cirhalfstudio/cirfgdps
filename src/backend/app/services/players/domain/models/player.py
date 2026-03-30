from dataclasses import dataclass, field
from datetime import UTC, datetime
from random import randint
from typing import Self

from .....config import get_const
from ..exceptions import DeletedError
from ..value_objects import (
    Email,
    ProfileIcons,
    ProfileSettings,
    UserName,
)

const = get_const()


@dataclass(slots=True)
class Player:
    """class that represents a player"""

    player_id: int
    username: UserName
    hashed_password: str = field(repr=False, hash=False)
    email: Email
    is_active: bool = False
    icons: ProfileIcons = field(default_factory=ProfileIcons.default)
    settings: ProfileSettings = field(default_factory=ProfileSettings.default)
    registered_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    deleted_at: datetime | None = None

    @classmethod
    def create(cls, username: str, hashed_password: str, email: str) -> Self:
        """factory of new players"""
        return cls(
            player_id=randint(0, const.MAX_INT32_VALUE),
            username=UserName(username),
            hashed_password=hashed_password,
            email=Email(email),
        )

    def activate(self) -> None:
        """activate the player to allow him to login"""
        if self.deleted_at is not None:
            raise DeletedError("deleted player cannot be activated")

        self.is_active = True

    def delete(self) -> None:
        """soft delete the player"""
        if self.deleted_at is not None:
            return

        self.deleted_at = datetime.now(UTC)
