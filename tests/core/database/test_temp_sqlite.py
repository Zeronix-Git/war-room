import pytest

from war_room.core.custom_types import User
from war_room.core.database import SQLUserDatabase, TemporaryUserDatabase

user_database_factories = {'temp': lambda: TemporaryUserDatabase(), 'sqlite': lambda: SQLUserDatabase(':memory:')}

err_msg = "Unexpected error"


@pytest.mark.parametrize('user_db_factory', user_database_factories.values(), ids=user_database_factories.keys())
def test_contains(user_db_factory):
    user_db = user_db_factory()
    print(user_db.contains(0))
    assert not user_db.contains(0).expect(err_msg)
    user = User(id=0)
    assert user_db.update(user).is_ok
    assert user_db.contains(0).expect(err_msg)


@pytest.mark.parametrize('user_db_factory', user_database_factories.values(), ids=user_database_factories.keys())
def test_get_user(user_db_factory):
    user_db = user_db_factory()
    user = User(id=0)
    assert user_db.update(user).is_ok
    user = user_db.get(0).expect(err_msg).expect(err_msg)
    assert user.id == 0


@pytest.mark.parametrize('user_db_factory', user_database_factories.values(), ids=user_database_factories.keys())
def test_iter_db(user_db_factory):
    user_db = user_db_factory()
    user = User(id=0)
    users = [User(id=0), User(id=1), User(id=2)]

    for user in users:
        assert user_db.update(user).is_ok

    user_ids = set()
    for maybe_user in user_db:
        user_ids.add(maybe_user.expect(err_msg).id)
    assert user_ids == set([0, 1, 2])


@pytest.mark.parametrize('user_db_factory', user_database_factories.values(), ids=user_database_factories.keys())
def test_update_user_information(user_db_factory):
    user_db = user_db_factory()
    user = User(id=0)
    assert user_db.update(user).is_ok
    user = user_db.get(0).expect(err_msg).expect(err_msg)
    user.game_count = 1
    assert user_db.update(user).is_ok
    user = user_db.get(0).expect(err_msg).expect(err_msg)
    assert user.game_count == 1
