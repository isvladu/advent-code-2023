from abc import ABC, abstractmethod

class SolutionBase(ABC):
    def read_input(self, day: int, input_no: str):
        with open("input/day" + str(day) + "_" + input_no + ".txt", "r") as f:
            self.input = f.read().splitlines()
        f.close()

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass