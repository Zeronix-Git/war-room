from war_room.core.custom_types.match import Match, MatchStatus, Tier


def test_to_from_dict():
    match = Match(
        id=0,
        p1_user_id=0,
        p1_commander='',
        p2_user_id=0,
        p2_commander='',
        map_id=0,
        tier=Tier.T1,
        pref_id=0,
        game_url='',
        status=MatchStatus.NOT_STARTED,
    )
    dict = match.to_dict()
    match2 = Match.from_dict(dict)
    assert match == match2
