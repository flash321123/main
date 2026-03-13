"""
Tests for calculator.py (人数牌算力)
"""

import pytest
from calculator import calculate_power, calculate_power_from_hands


class TestCalculatePower:
    def test_basic(self):
        result = calculate_power(num_players=4, cards_per_player=13)
        assert result["num_players"] == 4
        assert result["cards_per_player"] == 13
        assert result["power_per_player"] == 13 * 4
        assert result["total_power"] == 13 * 4 * 4

    def test_single_player(self):
        result = calculate_power(num_players=1, cards_per_player=5)
        assert result["power_per_player"] == 5
        assert result["total_power"] == 5

    def test_zero_cards(self):
        result = calculate_power(num_players=3, cards_per_player=0)
        assert result["power_per_player"] == 0
        assert result["total_power"] == 0

    def test_invalid_num_players_zero(self):
        with pytest.raises(ValueError):
            calculate_power(num_players=0, cards_per_player=5)

    def test_invalid_num_players_negative(self):
        with pytest.raises(ValueError):
            calculate_power(num_players=-1, cards_per_player=5)

    def test_invalid_cards_negative(self):
        with pytest.raises(ValueError):
            calculate_power(num_players=2, cards_per_player=-1)

    def test_large_values(self):
        result = calculate_power(num_players=100, cards_per_player=1000)
        assert result["power_per_player"] == 100_000
        assert result["total_power"] == 10_000_000


class TestCalculatePowerFromHands:
    def test_basic(self):
        result = calculate_power_from_hands([13, 13, 13, 13])
        assert result["num_players"] == 4
        assert result["powers"] == [52, 52, 52, 52]
        assert result["total_power"] == 208

    def test_uneven_hands(self):
        result = calculate_power_from_hands([5, 10, 15])
        assert result["num_players"] == 3
        assert result["powers"] == [15, 30, 45]
        assert result["total_power"] == 90

    def test_single_player(self):
        result = calculate_power_from_hands([7])
        assert result["num_players"] == 1
        assert result["powers"] == [7]
        assert result["total_power"] == 7

    def test_zero_cards(self):
        result = calculate_power_from_hands([0, 0, 0])
        assert result["total_power"] == 0

    def test_empty_hands_raises(self):
        with pytest.raises(ValueError):
            calculate_power_from_hands([])

    def test_negative_count_raises(self):
        with pytest.raises(ValueError):
            calculate_power_from_hands([5, -1, 3])

    def test_hands_preserved(self):
        hands = [3, 6, 9]
        result = calculate_power_from_hands(hands)
        assert result["hands"] == [3, 6, 9]
        # Ensure original list is not mutated
        assert hands == [3, 6, 9]
