from collections import Counter
from typing import Dict

from utils.solution_base import SolutionBase

card_values_pt_1 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 12,
    "Q": 13,
    "K": 14,
    "A": 15,
}

card_values_pt_2 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 13,
    "K": 14,
    "A": 15,
}


class Hand:
    def __init__(self, hand: str, value: int, card_values: Dict[str, int]) -> None:
        self.hand = hand
        self.value = value
        self.card_values = card_values
        self.card_freq = Counter(self.hand)

    def __repr__(self) -> str:
        return f"Hand({self.hand}, {self.value})"

    def get_hand_type(self):
        fst = list(self.card_freq.most_common())[0][1]
        try:
            snd = list(self.card_freq.most_common())[1][1]
        except IndexError:
            snd = 0

        if fst == 5:
            return 6
        elif fst == 4:
            return 5
        elif fst == 3 and snd == 2:
            return 4
        elif fst == 3 and snd == 1:
            return 3
        elif fst == 2 and snd == 2:
            return 2
        elif fst == 2 and snd == 1:
            return 1
        else:
            return 0

    def __lt__(self, other):
        if self.get_hand_type() < other.get_hand_type():
            return True
        elif self.get_hand_type() > other.get_hand_type():
            return False
        else:
            for i in range(0, 5):
                if self.card_values[self.hand[i]] != self.card_values[other.hand[i]]:
                    return (
                        self.card_values[self.hand[i]] < self.card_values[other.hand[i]]
                    )

        return False

    def __le__(self, other):
        if self.get_hand_type() < other.get_hand_type():
            return True
        elif self.get_hand_type() > other.get_hand_type():
            return False
        else:
            for i in range(0, 5):
                if self.card_values[self.hand[i]] != self.card_values[other.hand[i]]:
                    return (
                        self.card_values[self.hand[i]] < self.card_values[other.hand[i]]
                    )

        return True

    def __gt__(self, other):
        if self.get_hand_type() < other.get_hand_type():
            return False
        elif self.get_hand_type() > other.get_hand_type():
            return True
        else:
            for i in range(0, 5):
                if self.card_values[self.hand[i]] != self.card_values[other.hand[i]]:
                    return (
                        self.card_values[self.hand[i]] > self.card_values[other.hand[i]]
                    )

        return False

    def __ge__(self, other):
        if self.get_hand_type() < other.get_hand_type():
            return False
        elif self.get_hand_type() > other.get_hand_type():
            return True
        else:
            for i in range(0, 5):
                if self.card_values[self.hand[i]] != self.card_values[other.hand[i]]:
                    return (
                        self.card_values[self.hand[i]] > self.card_values[other.hand[i]]
                    )

        return True

    def __eq__(self, other):
        if self.get_hand_type != other.get_hand_type():
            return False
        else:
            for i in range(0, 5):
                if self.card_values[self.hand[i]] != self.card_values[other.hand[i]]:
                    return False

        return True


class Solution(SolutionBase):
    def parse_input(self):
        self.data_pt_1 = []
        self.data_pt_2 = []

        for line in self.input:
            hand = line.split(" ")[0]
            value = int(line.split(" ")[1])
            self.data_pt_1.append(Hand(hand, value, card_values_pt_1))
            self.data_pt_2.append(Hand(hand, value, card_values_pt_2))

    def solve_part1(self):
        sorted_hands = sorted(self.data_pt_1)
        res = 0

        for i, hand in enumerate(sorted_hands, start=1):
            res += hand.value * i

        return res

    def solve_part2(self):
        for hand in self.data_pt_2:
            if "J" in hand.hand:
                if hand.hand == "JJJJJ":
                    continue
                elif hand.card_freq.most_common()[0][0] != "J":
                    hand.card_freq.update(
                        hand.card_freq.most_common()[0][0] * hand.card_freq["J"]
                    )
                    hand.card_freq["J"] = 0
                else:
                    hand.card_freq.update(
                        hand.card_freq.most_common()[1][0] * hand.card_freq["J"]
                    )
                    hand.card_freq["J"] = 0

        sorted_hands = sorted(self.data_pt_2)
        res = 0

        for i, hand in enumerate(sorted_hands, start=1):
            res += hand.value * i

        return res
