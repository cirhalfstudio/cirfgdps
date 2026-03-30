from dataclasses import dataclass

from ....shared.domain import DomainError


@dataclass(slots=True)
class InvalidLengthError(DomainError):
    message = "InvalidLengthError"


@dataclass(slots=True)
class InvalidKeyError(DomainError):
    message = "InvalidKeyError"


@dataclass(slots=True)
class InvalidValueError(DomainError):
    message = "InvalidValueError"


@dataclass(slots=True)
class DeletedError(DomainError):
    message = "DeletedError"
