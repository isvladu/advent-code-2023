import re
from typing import List

from utils.solution_base import SolutionBase


class Card:
    def __init__(self, id: int, winning_numbers: List[int], my_numbers: List[int]) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers


class Solution(SolutionBase):
    card_list: List[Card]

    def parse_input(self):
        self.card_list = []

        for line in self.input:
            card = line.split(":")
            card_id = int(card[0][4:])
            numbers = card[1].split("|")
            winning_numbers = list(
                map(int, filter(lambda x: x != "", re.split("\s+", numbers[0])))
            )
            elf_numbers = list(
                map(int, filter(lambda x: x != "", re.split("\s+", numbers[1])))
            )
            self.card_list.append(Card(card_id, winning_numbers, elf_numbers))

    def solve_part1(self):
        res = 0

        for card in self.card_list:
            points = 0

            for number in card.my_numbers:
                if number in card.winning_numbers:
                    if points == 0:
                        points = 1
                    else:
                        points = points * 2

            res += points

        return res

    def solve_part2(self):
        res = 0

        card_dict = {i: 1 for i in range(1, len(self.card_list) + 1)}

        for card in self.card_list:
            res += card_dict[card.id]
            
            winning_no = 0

            for number in card.my_numbers:
                if number in card.winning_numbers:
                    winning_no += 1
                    
            for i in range(1, winning_no + 1):
                card_dict[card.id + i] += card_dict[card.id]
                
        return res


if __name__ == "__main__":
    solution = Solution(4)
    solution.read_input()

    part1 = solution.solve_part1()
    part2 = solution.solve_part2()

    with open("output/day3.txt", "w") as f:
        f.write("Part 1: " + str(part1) + "\n")
        f.write("Part 2: " + str(part2))
    f.close()
