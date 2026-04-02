from string import whitespace
from typing import ClassVar


class Helpers:
    """utility class w/ general helper functions so I don't repeat yourself"""

    _clear_whitespace_trans_table: ClassVar[dict[int, int | None]] = str.maketrans(
        "", "", whitespace
    )

    @classmethod
    def clear_whitespace(cls, value: str) -> str:
        return value.translate(cls._clear_whitespace_trans_table)

    @staticmethod
    def trim(value: str) -> str:
        """trim sounds cooler so why not"""
        return value.strip()
