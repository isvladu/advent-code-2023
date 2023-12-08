import itertools
import re
from functools import reduce
from math import gcd
from typing import Dict

from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    node_map: Dict[str, Dict]

    def __init__(self, day: int, input_type: str, part: int):
        self.node_map = {}
        super().__init__(day, input_type, part)
        
    @staticmethod
    def lcm(numbers):
        return reduce(lambda x, y: x * y // gcd(x, y), numbers, 1)

    def parse_input(self):
        self.instructions = self.input[0]

        for line in self.input[2:]:
            node = line.split("=")[0].replace(" ", "")
            l = line.split("=")[1].split(",")[0].replace(" (", "")
            r = line.split("=")[1].split(",")[1].replace(" ", "").replace(")", "")
            self.node_map[node] = {"L": l, "R": r}

    def solve_part1(self):
        start = "AAA"
        end = "ZZZ"
        curr = start
        steps = 0

        for instruction in itertools.cycle(self.instructions):
            if curr == end:
                return steps

            curr = self.node_map[curr][instruction]
            steps += 1

    def solve_part2(self):
        start_nodes = [node for node in list(self.node_map) if node[2] == "A"]
        end_nodes = [node for node in list(self.node_map) if node[2] == "Z"]
        current_nodes = start_nodes
        steps = [0] * len(start_nodes)
        found = [False] * len(start_nodes)
        curr_step = 0
        
        for instruction in itertools.cycle(self.instructions):
            if all(x > 0 for x in steps):
                return Solution.lcm(steps)
            
            for i in range(0, len(start_nodes)):
                if current_nodes[i] in end_nodes and not found[i]:
                    steps[i] = curr_step
                    found[i] = True
                    # print(f"Found {start_nodes[i]} at step: {curr_step}")

            temp = current_nodes
            current_nodes = [self.node_map[node][instruction] for node in temp]
            curr_step += 1
