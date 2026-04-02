import pytest

from src.backend.app.services.players.domain.exceptions import (
    InvalidLengthError,
    InvalidValueError,
)
from src.backend.app.services.players.domain.value_objects import (
    UserName,
)


async def test_create_username_success():
    assert UserName("ril")  # minimum length
    assert UserName("ril" * 11)  # maximum length
    assert UserName("   ril 7 3   \t  \n").value == "ril 7 3"  # test trim
    assert UserName("r-il_7.3")


async def test_create_username_failure():
    with pytest.raises(InvalidLengthError):
        UserName("73")
        UserName("ril73" * 7)
    with pytest.raises(InvalidValueError):
        UserName("рил73")
        UserName("  \t \n ")
