from dataclasses import dataclass

from ....shared.domain import DomainError


@dataclass
class InvalidLengthError(DomainError):
    message = "InvalidLengthError"


@dataclass
class InvalidKeyError(DomainError):
    message = "InvalidKeyError"


@dataclass
class InvalidValueError(DomainError):
    message = "InvalidValueError"


@dataclass
class DeletedError(DomainError):
    message = "DeletedError"
