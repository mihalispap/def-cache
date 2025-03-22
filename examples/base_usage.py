from def_cache import decorator

"""
The decorator below will cache the results of method: add for 60s in a file stored in the tmp relative path
"""
@decorator.cache(ttl=60, backend='fs', storage='tmp')
def add(x, y):
    return x + y

# this will not be called from cache
print(add(1, 2))

# this will be retrieved from cache
print(add(1, 2))
