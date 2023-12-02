from utils.solution_base import SolutionBase

digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


class Solution(SolutionBase):
    @staticmethod
    def is_substr_numeric(str: str):
        return str in digit_map.keys()

    def find_calibration_value(self, line: str):
        i = 0
        first = False
        last = False
        value = ""

        while i < len(line):
            if line[i].isnumeric() and not first:
                value = line[i] + value
                first = True
            if line[-i - 1].isnumeric() and not last:
                value = value + line[-i - 1]
                last = True
            if first and last:
                return int(value)

            i += 1

    def calibrate_line(self, line: str):
        i = 0
        new_line = line

        while i < len(new_line):
            try:
                if Solution.is_substr_numeric(new_line[i : i + 3]):
                    new_line = (
                        new_line[: i + 1]
                        + digit_map[new_line[i : i + 3]]
                        + new_line[i + 1 :]
                    )
                if Solution.is_substr_numeric(new_line[i : i + 4]):
                    new_line = (
                        new_line[: i + 2]
                        + digit_map[new_line[i : i + 4]]
                        + new_line[i + 2 :]
                    )
                if Solution.is_substr_numeric(new_line[i : i + 5]):
                    new_line = (
                        new_line[: i + 2]
                        + digit_map[new_line[i : i + 5]]
                        + new_line[i + 2 :]
                    )
            except KeyError:
                pass
            
            i += 1

        return new_line

    def solve_part1(self):
        sum_cv = 0
        for line in self.input:
            sum_cv += self.find_calibration_value(line)

        return sum_cv
    
    def solve_part2(self):
        sum_cv = 0
        for line in self.input:
            sum_cv += self.find_calibration_value(self.calibrate_line(line))
            
        return sum_cv


if __name__ == "__main__":
    solution = Solution()
    solution.read_input(1, "1")

    sum_cv_1 = solution.solve_part1()
    sum_cv_2 = solution.solve_part2()

    with open("output/day1.txt", "w") as f:
        f.write("Part 1: " + str(sum_cv_1) + "\n")
        f.write("Part 2: " + str(sum_cv_2))
    f.close()
