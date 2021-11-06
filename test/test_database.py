import pytest
from war_room.core.database import SQLiteUserDatabase, TemporaryUserDatabase

user_database_factories = (
    lambda: TemporaryUserDatabase(),
    lambda: SQLiteUserDatabase(':memory:')
)

@pytest.mark.parametrize('user_db_factory', user_database_factories)
def test_contains_user(user_db_factory):
    user_db = user_db_factory()
    assert not user_db.contains_user(0)
    user_db.register_user(0)
    assert user_db.contains_user(0)

@pytest.mark.parametrize('user_db_factory', user_database_factories)
def test_get_user(user_db_factory):
    user_db = user_db_factory()
    user_db.register_user(0)
    user = user_db.get_user(0)
    assert user.discord_id == 0

@pytest.mark.parametrize('user_db_factory', user_database_factories)
def test_update_user_information(user_db_factory):
    user_db = user_db_factory()
    user_db.register_user(0)
    user = user_db.get_user(0)
    user.game_count = 1
    user_db.update_user_information(user)
    user = user_db.get_user(0)
    assert user.game_count == 1
