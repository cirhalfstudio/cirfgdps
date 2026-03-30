from ctypes import c_int32
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Constants(BaseSettings):
    """class w/ reusable constant values so I don't repeat yourself"""

    USERNAME_MIN_LENGTH: int = 3
    USERNAME_MAX_LENGTH: int = 33  # TODO: actual gd username length limit
    USERNAME_PATTERN: str = r"^[a-zA-Z0-9_.- ]"

    EMAIL_MIN_LENGTH: int = 5
    EMAIL_MAX_LENGTH: int = 100  # TODO: actual gd email length limit
    EMAIL_PATTERN: str = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    MAX_INT32_VALUE: int = c_int32(-1).value

    model_config = SettingsConfigDict(env_file=None)


@lru_cache
def get_const() -> Constants:
    return Constants()
