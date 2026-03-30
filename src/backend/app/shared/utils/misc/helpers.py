from string import whitespace
from typing import ClassVar


class Helpers:
    """utility class w/ general helper functions so I don't repeat yourself"""

    _trim_trans_table: ClassVar[dict[int, int | None]] = str.maketrans(
        "", "", whitespace
    )

    @classmethod
    def trim(cls, value: str) -> str:
        """
        basically upgraded strip.
        also trim sounds cooler so why not
        """
        return value.translate(cls._trim_trans_table)
