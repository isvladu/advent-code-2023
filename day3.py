from utils.solution_base import SolutionBase

class Solution(SolutionBase):
    def solve_part1(self):
        pass

    def solve_part2(self):
        pass


if __name__ == "__main__":
    solution = Solution()
    solution.read_input(3, "train")

    part1 = solution.solve_part1()
    part2 = solution.solve_part2()

    with open("output/day3.txt", "w") as f:
        f.write("Part 1: " + str(part1) + "\n")
        f.write("Part 2: " + str(part2))
    f.close()
