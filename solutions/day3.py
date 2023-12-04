import itertools
from math import prod
from typing import List

from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    adj_map = {
        0: (-1, -1),
        1: (-1, 0),
        2: (-1, 1),
        3: (0, -1),
        4: (0, 1),
        5: (1, -1),
        6: (1, 0),
        7: (1, 1),
    }

    def is_valid_pos(self, i: int, j: int) -> bool:
        if i < 0 or j < 0 or i > len(self.input) - 1 or j > len(self.input) - 1:
            return False
        return True

    def get_valid_moves(self, row: int, col: int) -> List[str]:
        valid_moves_list = []
        moves = list(
            itertools.product([row - 1, row, row + 1], [col - 1, col, col + 1])
        )
        moves.remove((row, col))

        for move in moves:
            if self.is_valid_pos(move[0], move[1]):
                valid_moves_list.append(self.input[move[0]][move[1]])
            else:
                valid_moves_list.append(".")

        return valid_moves_list

    def is_an_adjacent_part(self, row: int, col: int) -> bool:
        return any(
            filter(
                lambda ch: not ch.isdigit() and not ch == ".",
                self.get_valid_moves(row, col),
            )
        )

    def is_an_adjacent_part_with_gear(self, row: int, col: int):
        adj_list = [ch for ch in self.get_valid_moves(row, col)]
        try:
            index = adj_list.index("*")
            x = row + self.adj_map[index][0]
            y = col + self.adj_map[index][1]
            return (True, x, y)
        except ValueError:
            return (False, -1, -1)

    def parse_input(self):
        pass

    def solve_part1(self):
        part_list = []

        for row, line in enumerate(self.input):
            current_number = ""
            is_adj = False

            for col, c in enumerate(line):
                if c.isdigit():
                    current_number += c
                    is_adj = is_adj or self.is_an_adjacent_part(row, col)
                elif is_adj:
                    part_list.append(int(current_number))
                    current_number = ""
                    is_adj = False
                else:
                    current_number = ""

            if current_number != "" and is_adj:
                part_list.append(int(current_number))

        return sum(part_list)

    def solve_part2(self):
        gear_map = {}
        res = 0

        for row, line in enumerate(self.input):
            current_number = ""
            is_adj = False
            current_gear = (-1, -1)

            for col, c in enumerate(line):
                if c.isdigit():
                    current_number += c
                    value, x, y = self.is_an_adjacent_part_with_gear(row, col)
                    if value:
                        is_adj = True
                        current_gear = (x, y)
                elif is_adj:
                    try:
                        gear_map[current_gear].append(int(current_number))
                    except KeyError:
                        gear_map[current_gear] = [int(current_number)]
                    current_number = ""
                    current_gear = (-1, -1)
                    is_adj = False
                else:
                    current_number = ""

            if current_number != "" and is_adj:
                try:
                    gear_map[current_gear].append(int(current_number))
                except KeyError:
                    gear_map[current_gear] = [int(current_number)]

        for gear, numbers in gear_map.items():
            if len(numbers) > 1:
                res += prod(numbers)

        return res


if __name__ == "__main__":
    solution = Solution(3)
    solution.read_input()

    part1 = solution.solve_part1()
    part2 = solution.solve_part2()

    with open("output/day3.txt", "w") as f:
        f.write("Part 1: " + str(part1) + "\n")
        f.write("Part 2: " + str(part2))
    f.close()
