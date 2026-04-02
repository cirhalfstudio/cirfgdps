import pytest

from src.backend.app.services.players.domain.exceptions import (
    InvalidLengthError,
    InvalidValueError,
)
from src.backend.app.services.players.domain.value_objects import Email


async def test_create_email_success():
    assert Email("7@3.cf")  # minimum length
    assert Email("ril@7." + "cirf" * 21)  # maximum length
    assert Email("   ril@73.cirf   \t  \n").value == "ril@73.cirf"  # test trim
    assert Email("r-i.l+_@ril7-3.cirf")


async def test_create_email_failure():
    with pytest.raises(InvalidLengthError):
        Email("ril@73.cirf" * 10)
    with pytest.raises(InvalidValueError):
        Email("рил@73.сирф")
        Email("  \t \n ")
