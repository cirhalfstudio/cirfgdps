from datetime import datetime

from pydantic import BaseModel, ConfigDict

from ...domain.value_objects import SettingType


class PlayerDTO(BaseModel):
    """class that represents the data transfer object of a player"""

    player_id: int
    username: str
    email: str
    is_active: bool
    icons: dict[str, int]
    settings: dict[str, SettingType]
    registered_at: datetime
    deleted_at: datetime | None

    model_config = ConfigDict(from_attributes=True, frozen=True)
