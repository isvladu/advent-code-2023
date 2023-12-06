import re

from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def parse_input(self):
        self.times = list(map(int, re.split("\s+", self.input[0].split(":")[1])[1:]))
        self.distances = list(
            map(int, re.split("\s+", self.input[1].split(":")[1])[1:])
        )

        get_time_part2 = lambda x: int("".join(str(i) for i in x))
        get_distance_part2 = lambda x: int("".join(str(i) for i in x))
        self.time_part2 = get_time_part2(self.times)
        self.distance_part2 = get_distance_part2(self.distances)

    def solve_part1(self):
        res = 1

        for i in range(len(self.times)):
            result_times = list(
                filter(
                    lambda x: x > self.distances[i],
                    [j * (self.times[i] - j) for j in range(0, self.times[i])],
                )
            )
            res *= len(result_times)

        return res

    def solve_part2(self):
        for i in range(0, self.time_part2):
            if i * (self.time_part2 - i) > self.distance_part2:
                fst = i
                lst = self.time_part2 - i
                break

        return lst - fst + 1
