from ...domain.models import Player
from ...domain.value_objects import Email, ProfileIcons, ProfileSettings, UserName
from ..db_models import DBPlayer
from ..dto import PlayerDTO


class PlayerMapper:
    """class used to map three types of player models across the backend"""

    @staticmethod
    def to_domain(db_player: DBPlayer) -> Player:
        """map player from orm model to domain model"""

        return Player(
            player_id=db_player.player_id,
            username=UserName(db_player.username),
            hashed_password=db_player.hashed_password,
            email=Email(db_player.email),
            is_active=db_player.is_active,
            icons=ProfileIcons.from_dict(db_player.icons),
            settings=ProfileSettings.from_dict(db_player.settings),
            registered_at=db_player.registered_at,
            deleted_at=db_player.deleted_at,
        )

    @staticmethod
    def to_orm(player: Player) -> DBPlayer:
        """map player from domain model to orm model"""

        return DBPlayer(
            player_id=player.player_id,
            username=player.username.value,
            hashed_password=player.hashed_password,
            email=player.email.value,
            is_active=player.is_active,
            icons=player.icons.view().copy(),
            settings=player.settings.view().copy(),
            registered_at=player.registered_at,
            deleted_at=player.deleted_at,
        )

    @staticmethod
    def to_dto(player: Player) -> PlayerDTO:
        """map player from domain model to data transfer object"""

        return PlayerDTO(
            player_id=player.player_id,
            username=player.username.value,
            email=player.email.value,
            is_active=player.is_active,
            icons=player.icons.view().copy(),
            settings=player.settings.view().copy(),
            registered_at=player.registered_at,
            deleted_at=player.deleted_at,
        )
