from ctypes import c_int32
from datetime import UTC, datetime
from random import randint
from typing import Any

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .....shared.utils.db import Base


class DBPlayer(Base):
    __tablename__ = "players"

    player_id: Mapped[int] = mapped_column(
        primary_key=True,
        default=lambda: randint(0, c_int32(-1).value),  # max int32 value
    )
    username: Mapped[str] = mapped_column(
        String(33),  # TODO: actual gd username length limit
        nullable=False,
        unique=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(100),  # TODO: actual gd email length limit
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
        default=dict,  # TODO // FIXME
    )
    settings_json: Mapped[dict[str, Any]] = mapped_column(
        JSONB,
        nullable=False,
        default=dict,  # TODO // FIXME
    )
    registered_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        default=None,
    )
