import argparse
import importlib
import os
import unittest


class Runner:
    def __init__(self, day: str | None = None, skip_tests: bool = False):
        if day:
            self.day = day
        else:
            self.day = self.get_last_day()
        if skip_tests:
            self.run_tests = False
        else:
            self.run_tests = True

    def get_last_day(self) -> int:
        last_day = 0

        for i in range(1, 26):
            if os.path.exists(f"solutions/day{i}.py") and i > last_day:
                last_day = i

        return last_day

    def run(self):
        if self.run_tests:
            suite = unittest.TestLoader().discover("tests", pattern="*_test.py")
            result = unittest.TextTestRunner(verbosity=2).run(suite)

        try:
            part1 = importlib.import_module(f"solutions.day{self.day}").Solution(
                self.day, "prod", 1
            )
            part2 = importlib.import_module(f"solutions.day{self.day}").Solution(
                self.day, "prod", 2
            )
        except ModuleNotFoundError:
            print(f"Error! Module for day {self.day} not found!")

        print(f"Day {self.day} solutions")
        print(f"=====================")
        print(f"Part 1: {part1.solve_part1()}")
        print(f"Part 2: {part2.solve_part2()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Advent of Code 2023 Solver",
        description="Runs a specific day from the set of AoC2023 problems",
        epilog="isvladu",
    )

    parser.add_argument(
        "-d",
        "--day",
        dest="day",
        metavar="day_number",
        type=int,
        help="Optional, day number of AoC, if not present runs last available day",
    )
    parser.add_argument(
        "--skip-tests", action="store_true", help="Optional, skipping tests"
    )

    args = parser.parse_args()

    app = Runner(args.day, args.skip_tests)
    app.run()


# TODO: finish implementing the solution_base runner and rewrite
