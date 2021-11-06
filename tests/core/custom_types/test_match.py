from war_room.core.custom_types import Match, MatchStatus


def test_to_from_dict():
    match = Match(id=0, p1_user_id=0, p2_user_id=1, tier=0, status=MatchStatus.NOT_STARTED)
    dict = match.to_dict()
    match2 = Match.from_dict(dict)
    assert match == match2
