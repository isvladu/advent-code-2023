class Solution:
    def read_input(self):
        with open("input/day2_1.txt", "r") as f:
            input = f.read().splitlines()
        f.close()

    def solve_part1(self):
        pass

    def solve_part2(self):
        pass


if __name__ == "__main__":
    solution = Solution()
    solution.read_input()

    part1 = solution.solve_part1()
    part2 = solution.solve_part2()

    with open("output/day2.txt", "w") as f:
        f.write("Part 1: " + str(part1) + "\n")
        f.write("Part 2: " + str(part2))
    f.close()
