#!/usr/bin/env python3
"""
人数牌算力 - Card/Tile Computing Power Calculator CLI
"""

import sys
from calculator import calculate_power, calculate_power_from_hands


def main():
    print("=== 人数牌算力 ===")
    print("Card/Tile Computing Power Calculator\n")

    args = sys.argv[1:]

    # Mode 1: uniform cards - usage: main.py <num_players> <cards_per_player>
    #         Requires exactly 2 arguments.
    if len(args) == 2:
        try:
            num_players = int(args[0])
            cards_per_player = int(args[1])
        except ValueError:
            print("错误: 请输入整数参数 (Error: arguments must be integers)")
            sys.exit(1)
        result = calculate_power(num_players, cards_per_player)
        _print_uniform_result(result)

    # Mode 2: individual hands - usage: main.py <c1> [c2 ... cN]
    #         Accepts 1 or more arguments, each being one player's card count.
    elif len(args) >= 1:
        try:
            hands = [int(a) for a in args]
        except ValueError:
            print("错误: 请输入整数参数 (Error: arguments must be integers)")
            sys.exit(1)
        result = calculate_power_from_hands(hands)
        _print_hands_result(result)

    # Interactive mode
    else:
        _interactive()


def _print_uniform_result(result: dict):
    print(f"玩家人数 (Players):       {result['num_players']}")
    print(f"每人牌数 (Cards/player):  {result['cards_per_player']}")
    print(f"每人算力 (Power/player):  {result['power_per_player']}")
    print(f"总算力   (Total power):   {result['total_power']}")


def _print_hands_result(result: dict):
    print(f"玩家人数 (Players): {result['num_players']}")
    for i, (hand, power) in enumerate(zip(result["hands"], result["powers"]), 1):
        print(f"  玩家 {i} (Player {i}): 牌数={hand}, 算力={power}")
    print(f"总算力 (Total power): {result['total_power']}")


def _interactive():
    try:
        num_players = int(input("请输入玩家人数 (Enter number of players): "))
        mode = input(
            "每人相同牌数? (Same cards per player?) [y/n]: "
        ).strip().lower()

        if mode == "y":
            cards = int(input("请输入每人牌数 (Enter cards per player): "))
            result = calculate_power(num_players, cards)
            print()
            _print_uniform_result(result)
        else:
            hands = []
            for i in range(1, num_players + 1):
                c = int(input(f"请输入玩家 {i} 的牌数 (Cards for player {i}): "))
                hands.append(c)
            result = calculate_power_from_hands(hands)
            print()
            _print_hands_result(result)
    except (ValueError, EOFError) as exc:
        if isinstance(exc, ValueError) and not str(exc).startswith("invalid literal"):
            # Domain validation errors are already in Chinese/English
            print(f"错误 (Error): {exc}")
        else:
            print("输入无效 (Invalid input): 请输入有效的整数 (please enter valid integers)")
        sys.exit(1)


if __name__ == "__main__":
    main()
