"""
人数牌算力 - Card/Tile Computing Power Calculator

Calculate the total and per-player computing power based on
the number of players and their card/tile counts.
"""


def calculate_power(num_players: int, cards_per_player: int) -> dict:
    """
    Calculate the computing power when all players have the same number of cards.

    Args:
        num_players: Number of players (人数), must be >= 1
        cards_per_player: Number of cards/tiles each player holds (牌), must be >= 0

    Returns:
        A dict with:
            - 'num_players': number of players
            - 'cards_per_player': cards each player has
            - 'power_per_player': computing power per player
            - 'total_power': total computing power across all players

    Raises:
        ValueError: if num_players < 1 or cards_per_player < 0
    """
    if num_players < 1:
        raise ValueError("人数必须大于等于1 (num_players must be >= 1)")
    if cards_per_player < 0:
        raise ValueError("每人牌数不能为负数 (cards_per_player must be >= 0)")

    power_per_player = cards_per_player * num_players
    total_power = power_per_player * num_players

    return {
        "num_players": num_players,
        "cards_per_player": cards_per_player,
        "power_per_player": power_per_player,
        "total_power": total_power,
    }


def calculate_power_from_hands(hands: list) -> dict:
    """
    Calculate computing power from a list of individual player hands.

    Args:
        hands: A list of card counts (one entry per player). Each entry is
               the number of cards/tiles that player holds.

    Returns:
        A dict with:
            - 'num_players': number of players
            - 'hands': the original list of card counts
            - 'powers': list of per-player power scores
            - 'total_power': sum of all power scores

    Raises:
        ValueError: if hands is empty or any count is negative
    """
    if not hands:
        raise ValueError("手牌列表不能为空 (hands list must not be empty)")
    for i, count in enumerate(hands):
        if count < 0:
            raise ValueError(
                f"玩家 {i + 1} 的牌数不能为负数 (player {i + 1} card count must be >= 0)"
            )

    num_players = len(hands)
    powers = [count * num_players for count in hands]
    total_power = sum(powers)

    return {
        "num_players": num_players,
        "hands": list(hands),
        "powers": powers,
        "total_power": total_power,
    }
