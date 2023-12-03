from abc import ABC, abstractmethod


class SolutionBase(ABC):
    """Base class for the Solution implemented in each day

    Args:
        ABC (Abstract): Helper abstract class
    """

    def __init__(self, day: int, input_type: str, part: int):
        self._day = day
        self.input_type = input_type
        self.part = part
        self.read_input()
        self.parse_input()
        
    @property
    def day(self):
        return self._day

    def read_input(self):
        suffix = ""
        if self.input_type == "test":
            suffix = f"_train_{self.part}"
        with open(f"input/day{str(self._day)}{suffix}.txt", "r") as f:
            self.input = f.read().splitlines()
        f.close()
        
    @abstractmethod
    def parse_input(self):
        pass

    @abstractmethod
    def solve_part1(self):
        pass

    @abstractmethod
    def solve_part2(self):
        pass
