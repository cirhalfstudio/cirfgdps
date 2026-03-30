from datetime import datetime

from pydantic import BaseModel, ConfigDict

from ...domain.value_objects import ProfileIconsSchema, ProfileSettingsSchema


class PlayerDTO(BaseModel):
    """class that represents the data transfer object of a player"""

    player_id: int
    username: str
    email: str
    is_active: bool
    icons_json: ProfileIconsSchema
    settings_json: ProfileSettingsSchema
    registered_at: datetime
    deleted_at: datetime | None

    model_config = ConfigDict(from_attributes=True, frozen=True)
