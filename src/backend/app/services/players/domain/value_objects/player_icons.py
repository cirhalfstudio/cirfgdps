from dataclasses import dataclass
from enum import StrEnum
from types import MappingProxyType
from typing import ClassVar, Self, TypedDict

from ..exceptions import (
    InvalidValueError,
)


class IconKey(StrEnum):
    ICON = "icon"
    ICON_TYPE = "iconType"
    COLOR1 = "color1"
    COLOR2 = "color2"
    COLOR3 = "color3"
    SPECIAL = "special"
    CUBE = "acc_icon"
    SHIP = "acc_ship"
    BALL = "acc_ball"
    UFO = "acc_bird"
    WAVE = "acc_dart"
    ROBOT = "acc_robot"
    SPIDER = "acc_spider"
    SWING = "acc_swing"
    JETPACK = "acc_jetpack"
    GLOW = "acc_glow"
    EXPLOSION = "acc_explosion"


class ProfileIconsSchema(TypedDict):
    icon: int
    iconType: int
    color1: int
    color2: int
    color3: int
    special: int
    acc_icon: int
    acc_ship: int
    acc_ball: int
    acc_bird: int
    acc_dart: int
    acc_robot: int
    acc_spider: int
    acc_swing: int
    acc_jetpack: int
    acc_glow: int
    acc_explosion: int


@dataclass(slots=True)
class ProfileIcons:
    """class that represents the icons in a player's profile"""

    _icons: ProfileIconsSchema
    _default: ClassVar[ProfileIconsSchema] = {
        "icon": 0,
        "iconType": 0,
        "color1": 0,
        "color2": 0,
        "color3": 0,
        "special": 0,
        "acc_icon": 0,
        "acc_ship": 0,
        "acc_ball": 0,
        "acc_bird": 0,
        "acc_dart": 0,
        "acc_robot": 0,
        "acc_spider": 0,
        "acc_swing": 0,
        "acc_jetpack": 0,
        "acc_glow": 0,
        "acc_explosion": 0,
    }

    @classmethod
    def default(cls) -> Self:
        """
        factory of new profile icons.
        used in players factory
        """
        return cls(_icons=cls._default.copy())

    def get(self, key: IconKey) -> int:
        """get profile icon id by key"""
        return self._icons[key.value]

    def update(self, key: IconKey, value: int) -> None:
        """update profile icon id by key"""
        if value < 0:
            raise InvalidValueError("icon id cannot be negative")
        self._icons[key.value] = value

    def view(self) -> MappingProxyType[str, int]:
        """get an immutable readonly profile icons view"""
        return MappingProxyType(self._icons)  # type: ignore
