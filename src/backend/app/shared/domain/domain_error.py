from dataclasses import dataclass


@dataclass(slots=True)
class DomainError(Exception):
    """
    Base domain error.
    All domain errors must be inherited from this class.
    """

    message: str = "DomainError"
