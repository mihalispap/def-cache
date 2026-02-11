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


"""
The decorator below will cache the results of method: add for 60s in a file stored in the tmp relative path 
ignoring the 3rd parameter when attempting to cache
"""
@decorator.cache(ttl=60, backend='fs', storage='tmp', ignore_by_index=[2])
def add_ignore_by_index(x, y, z):
    return x + y

# this will not be called from cache
print(add_ignore_by_index(1, 2, -1))

# this will be retrieved from cache since parameter#3 is ignored
print(add_ignore_by_index(1, 2, -5))

"""
The decorator below will cache the results of method: add for 60s in a file stored in the tmp relative path 
ignoring the parameter name `z` when attempting to cache
"""
@decorator.cache(ttl=60, backend='fs', storage='tmp', ignore_by_name=['z'])
def add_ignore_by_name(x, y, z):
    return x + y

# this will not be called from cache
print(add_ignore_by_name(x=1, y=2, z=10))

# this will be retrieved from cache since z is ignored
print(add_ignore_by_name(x=1, y=2, z=15))
