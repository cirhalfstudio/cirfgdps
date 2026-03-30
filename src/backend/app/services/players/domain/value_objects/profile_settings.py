from dataclasses import dataclass
from enum import StrEnum
from types import MappingProxyType
from typing import ClassVar, Self, TypedDict

SettingType = bool | str | None


class SettingKey(StrEnum):
    MESSAGES_STATE = "mS"
    FRIEND_REQUESTS_STATE = "fS"
    COMMENTS_STATE = "cS"
    YOUTUBE = "yt"
    TWITTER = "twitter"
    TWITCH = "twitch"


class ProfileSettingsSchema(TypedDict):
    mS: bool
    fS: bool
    cS: bool
    yt: str | None
    twitter: str | None
    twitch: str | None


@dataclass(slots=True)
class ProfileSettings:
    """class that represents the settings of a player's profile"""

    _settings: ProfileSettingsSchema
    _default: ClassVar[ProfileSettingsSchema] = {
        "mS": False,
        "fS": False,
        "cS": False,
        "yt": None,
        "twitter": None,
        "twitch": None,
    }

    @classmethod
    def default(cls) -> Self:
        """
        factory of new profile settings.
        used in players factory
        """
        return cls(_settings=cls._default.copy())

    @classmethod
    def from_dict(cls, settings_dict: dict[str, SettingType]) -> Self:
        """
        load profile settings from dict
        """
        return cls(_settings=settings_dict.copy())  # type: ignore

    def get(self, key: SettingKey) -> SettingType:
        """get profile setting value by key"""
        return self._settings[key.value]

    def update(self, key: SettingKey, value: SettingType) -> None:
        """update profile setting value by key"""
        self._settings[key.value] = value  # type: ignore

    def view(self) -> MappingProxyType[str, SettingType]:
        """get an immutable readonly profile settings view"""
        return MappingProxyType(self._settings)  # type: ignore
