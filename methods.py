from players import soccer_db
from match import match
from typing import List, Tuple, Callable, Any

def get_player_name(player: Tuple[str, str, str, str, int]) -> str:
    return player[0]

def get_position(player: Tuple[str, str, str, str, int]) -> str:
    return player[1]

def get_club(player: Tuple[str, str, str, str, int]) -> str:
    return player[2]

def get_nationality(player: Tuple[str, str, str, str, int]) -> str:
    return player[3]

def get_goals(player: Tuple[str, str, str, str, int]) -> int:
    return player[4]

def player_by_nationality(matches: List[str]) -> List[str]:
    nationality = matches[0]
    result = []
    for player in soccer_db:
        if get_nationality(player) == nationality:
            result.append(get_player_name(player))
    return result

def player_by_club(matches: List[str]) -> List[str]:
    club = matches[0]
    result = []
    for player in soccer_db:
        if get_club(player) == club:
            result.append(get_player_name(player))
    return result

def players_by_position(matches: List[str]) -> List[str]:
    position = matches[0]
    result = []
    for player in soccer_db:
        if get_position(player) == position:
            result.append(get_player_name(player))
    return result

def top_scorers(matches: List[str]) -> List[str]:
    min_goals = int(matches[0])
    result = []
    for player in soccer_db:
        if get_goals(player) >= min_goals:
            result.append(get_player_name(player))
    return result

def player_goals(matches: List[str]) -> List[int]:
    player_name = matches[0]
    result = []
    for player in soccer_db:
        if get_player_name(player) == player_name:
            result.append(get_goals(player))
    return result