import hashlib
from copy import copy
from typing import Optional

from .model import models

ACCEPTABLE_BACKENDS = ['fs']


def _get_cache_entry() -> Optional[models.CacheEntry]:
    return None


def _create_cache_entry() -> models.CacheEntry:
    return models.CacheEntry()


def cache(
        ttl: int = -1,
        backend: str = 'fs',
        directory: Optional[str] = 'cache',
):
    def decorator(function):
        def wrapper(*args, **kwargs):
            assert (
                    backend in ACCEPTABLE_BACKENDS
            ), f'cache decorator expects one of: {ACCEPTABLE_BACKENDS} as backends'

            caller = f'{function.__module__}.{function.__name__}'
            params = copy(kwargs)
            params['args'] = args

            m = hashlib.md5()
            m.update((caller + str(params)).encode('utf-8'))

            cache_entry_id = m.hexdigest()
            cache_entry = _get_cache_entry()

            if not cache_entry:
                response = function(*args, **kwargs)
                cache_entry = _create_cache_entry()

            return None

        return wrapper

    return decorator
