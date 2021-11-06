from war_room.core.types import User

def test_to_from_dict():
    user = User(id = 0)
    dict = user.to_dict()
    user2 = User.from_dict(dict)
    assert user == user2