import pytest
from war_room.core.types import User
from war_room.core.database import SQLiteUserDatabase, TemporaryUserDatabase

user_database_factories = (
    lambda: TemporaryUserDatabase(),
    lambda: SQLiteUserDatabase(':memory:')
)

err_msg = "Unexpected error"

@pytest.mark.parametrize('user_db_factory', user_database_factories)
def test_contains_user(user_db_factory):
    user_db = user_db_factory()
    assert not user_db.contains_user(0).expect(err_msg)
    user = User(id = 0)
    assert user_db.update_user(user).is_ok
    assert user_db.contains_user(0).expect(err_msg)

@pytest.mark.parametrize('user_db_factory', user_database_factories)
def test_get_user(user_db_factory):
    user_db = user_db_factory()
    user = User(id = 0)
    assert user_db.update_user(user).is_ok
    user = user_db.get_user(0).expect(err_msg).expect(err_msg)
    assert user.id == 0

@pytest.mark.parametrize('user_db_factory', user_database_factories)
def test_update_user_information(user_db_factory):
    user_db = user_db_factory()
    user = User(id = 0) 
    assert user_db.update_user(user).is_ok
    user = user_db.get_user(0).expect(err_msg).expect(err_msg)
    user.game_count = 1
    assert user_db.update_user(user).is_ok
    user = user_db.get_user(0).expect(err_msg).expect(err_msg)
    assert user.game_count == 1
