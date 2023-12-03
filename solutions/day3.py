from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def parse_input(self):
        pass
    
    def solve_part1(self):
        pass

    def solve_part2(self):
        pass


if __name__ == "__main__":
    solution = Solution(3)
    solution.read_input()

    part1 = solution.solve_part1()
    part2 = solution.solve_part2()

    with open("output/day3.txt", "w") as f:
        f.write("Part 1: " + str(part1) + "\n")
        f.write("Part 2: " + str(part2))
    f.close()
