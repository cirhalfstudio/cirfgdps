from datetime import datetime

from src.backend.app.services.players.domain.models import Player
from src.backend.app.services.players.domain.value_objects import (
    Email,
    ProfileIcons,
    ProfileSettings,
    UserName,
)


async def test_player_create_success():
    username = "ril73"
    hashed_password = "73"
    email = "ril@73.cirf"
    player = Player.create(username, hashed_password, email)

    assert isinstance(player, Player)
    assert isinstance(player.player_id, int)
    assert isinstance(player.username, UserName)
    assert player.username.value == username
    assert player.hashed_password == hashed_password
    assert isinstance(player.email, Email)
    assert player.email.value == email
    assert player.is_active is False
    assert isinstance(player.icons, ProfileIcons)
    assert player.icons == ProfileIcons.default()
    assert isinstance(player.settings, ProfileSettings)
    assert player.settings == ProfileSettings.default()
    assert isinstance(player.registered_at, datetime)
    assert player.deleted_at is None
