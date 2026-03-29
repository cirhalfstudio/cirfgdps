from dishka import make_async_container

from .providers import (
    DBSessionProvider,
)

container = make_async_container(
    DBSessionProvider(),
)
