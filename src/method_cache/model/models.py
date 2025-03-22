import datetime
from typing import Generic, TypeVar

T = TypeVar('T')


class CacheEntry():
    id: str
    size: int
    result: Generic[T]
    created_at: datetime.datetime
