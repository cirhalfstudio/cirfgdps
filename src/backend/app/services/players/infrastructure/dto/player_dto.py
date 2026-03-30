from pydantic import BaseModel

from ...domain.value_objects import ProfileIconsSchema, ProfileSettingsSchema


class PlayerDTO(BaseModel):
    """class that represents the data transfer object of a player"""

    player_id: int
    username: str
    email: str
    is_active: bool
    icons_json: ProfileIconsSchema
    settings_json: ProfileSettingsSchema
