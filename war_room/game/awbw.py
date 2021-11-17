import requests
from option import Option, Result

from war_room.core.custom_types.match import Match, MatchDescription
from war_room.game.base import BaseGameHandler
from war_room.game.utils import random_string


def get_game_name(match_desc) -> str:
    return 'test'


def get_game_password(match_desc) -> str:
    return random_string(8)


def _login_to_awbw(session: requests.Session, username: str, password: str) -> requests.Response:
    """Login to AWBW and save the session cookie for future use"""
    return session.post(
        'https://awbw.amarriner.com/login.php',
        data={
            'username': username,
            'password': password,
            # 'url': 'https://awbw.amarriner.com/index.php',
        },
    )


def _create_private_game_without_joining(
    session: requests.Session, pref_id: int, name: str, password: str
) -> requests.Response:
    """Create a private game with given name and password.

    Requires session to have login cookie with Map Committee account
    to enable create without joining."""
    return session.post(
        'https://awbw.amarriner.com/create.php',
        params={'prefs_id': pref_id},
        data={
            'game_name': name,
            'game_password': password,
            'create': 'Create Game',
            'no_join': 1,
        },
    )


class AWBWGameHandler(BaseGameHandler):
    """Base class for handling AWBW games."""

    def __init__(self, awbw_username: str, awbw_password, str):
        """Init with AWBW login credentials.

        Account must be a Map Committee account so that it can create games without joining."""
        self.awbw_username = awbw_username
        self.awbw_password = awbw_password

    def create_game(self, match_desc: MatchDescription) -> Result[Match, str]:
        """Create an AWBW game

        Note on to manually derive parameters for the POST requests here:
        1. In Google Chrome, turn on Dev Tools with Ctrl + Shift + J
        2. Go to 'Network' tab and check 'Preserve log'
        3. Send the POST request by submitting the form (i.e. login / create game)
            - This records requests in history
        4. Filter history by method:POST
        5. Double click the relevant entry and view 'Headers' to see the contents of POST request
        """
        game_name = get_game_name(match_desc)
        game_password = get_game_password(match_desc)

        try:
            with requests.Session() as s:
                _login_response = _login_to_awbw(s, self.awbw_username, self.awbw_password)
                _creation_response = _create_private_game_without_joining(
                    s, match_desc.pref_id, game_name, game_password
                )
        except Exception as e:
            return Result.Err(str(e))

    def get_game_info(self, id: int) -> Result[Option[Match], str]:
        """Get information about an ongoing AWBW game

        Args:
            id: AWBW 6-digit game ID
        """
        return Result.Err('Not implemented yet')
