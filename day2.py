import re
from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    games = {}

    def parse_input(self):
        for game in self.input:
            game = re.sub(r" ", "", game)
            game_no, sets = game.split(":")
            game_id = int(re.sub(r"[^0-9]", "", game_no))
            sets = sets.split(";")
            self.games[game_id] = []
            for set in sets:
                (r, g, b) = self.parse_set(set)
                self.games[game_id].append((r, g, b))

    def parse_set(self, set: str):
        r, g, b = 0, 0, 0
        cubes = set.split(",")
        for cube in cubes:
            if "blue" in cube:
                b = int(re.sub(r"blue", "", cube))
            if "red" in cube:
                r = int(re.sub(r"red", "", cube))
            if "green" in cube:
                g = int(re.sub(r"green", "", cube))

        return (r, g, b)

    def solve_part1(self):
        result = 0

        for game_id, sets in self.games.items():
            valid_game = True

            for set in sets:
                if set[0] > 12 or set[1] > 13 or set[2] > 14:
                    valid_game = False
                    break

            if valid_game:
                result += game_id

        return result

    def solve_part2(self):
        result = 0

        for game_id, sets in self.games.items():
            max_r = 0
            max_g = 0
            max_b = 0
            for set in sets:
                if set[0] > max_r:
                    max_r = set[0]
                if set[1] > max_g:
                    max_g = set[1]
                if set[2] > max_b:
                    max_b = set[2]

            result += max_r * max_g * max_b
            
        return result


if __name__ == "__main__":
    solution = Solution()
    solution.read_input(2, "1")
    solution.parse_input()

    part1 = solution.solve_part1()
    part2 = solution.solve_part2()

    with open("output/day2.txt", "w") as f:
        f.write("Part 1: " + str(part1) + "\n")
        f.write("Part 2: " + str(part2))
    f.close()
