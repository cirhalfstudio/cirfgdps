from abc import ABC, abstractmethod

from ...domain.models import Player


class BasePlayerRepository(ABC):
    """abstract class that describes what should be implemented in player repository realizations"""

    @abstractmethod
    async def get_by_id(self, player_id: int) -> Player | None: ...

    @abstractmethod
    async def get_by_username(self, username: str) -> Player | None: ...

    @abstractmethod
    async def get_by_email(self, email: str) -> Player | None: ...

    @abstractmethod
    async def save(self, player: Player) -> None: ...

    @abstractmethod
    async def delete(self, player_id: int) -> None: ...
