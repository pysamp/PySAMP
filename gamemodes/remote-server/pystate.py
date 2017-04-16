""" Implements internal state for sa-mp servers,
so python gamemodes can be reloaded during runtime,
if used correctly """

STATE = {}
MIGRATIONS = {}

def add_migration(appid, field, default):
    """ adds a migration to the state """
    if not MIGRATIONS.has_key(appid):
        MIGRATIONS[appid] = default
    if not MIGRATIONS[appid].has_key(field):
        MIGRATIONS[appid][field] = default

def migrate():
    """ runs migrations """
    for _, migration in MIGRATIONS:
        for field, default in migration:
            if not STATE.has_key(field):
                STATE[field] = default

def get_state(appid, field):
    """ returns specific state variable """
    if MIGRATIONS.has_key(appid) and MIGRATIONS[appid].has_key(field):
        return MIGRATIONS[appid][field]
    return None

def set_state(appid, field):
    """ sets specific state variable, returns True if successful """
    if MIGRATIONS.has_key(appid) and MIGRATIONS[appid].has_key(field):
        return True
    return False
