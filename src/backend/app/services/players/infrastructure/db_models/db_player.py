from datetime import datetime
from typing import Any

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .....config import get_const
from .....shared.utils.db import Base

const = get_const()


class DBPlayer(Base):
    """class that represents a player in the database"""

    __tablename__ = "players"

    player_id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(
        String(const.USERNAME_MAX_LENGTH),
        nullable=False,
        unique=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(const.EMAIL_MAX_LENGTH),
        nullable=False,
        unique=True,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
    icons_json: Mapped[str] = mapped_column(
        JSONB,
        nullable=False,
    )
    settings_json: Mapped[dict[str, Any]] = mapped_column(
        JSONB,
        nullable=False,
    )
    registered_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        default=None,
    )
