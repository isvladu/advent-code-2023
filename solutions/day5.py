import re
from typing import List, Tuple

from utils.solution_base import SolutionBase


class Solution(SolutionBase):
    def parse_input(self):        
        self.seeds_part1 = self.parse_seeds_part1(self.input[0])
        self.seeds_part2 = self.parse_seeds_part2(self.input[0])
        self.map_list = self.parse_map(self.input)

    def parse_seeds_part1(self, line: str) -> List[int]:
        seeds = line.split(":")[1]
        seeds = list(map(int, filter(lambda x: x != "", re.split("\s+", seeds))))

        return seeds

    def parse_seeds_part2(self, line: str) -> List[int]:
        seeds = line.split(":")[1]
        line_parsed = list(map(int, filter(lambda x: x != "", re.split("\s+", seeds))))
        seeds = [
            (line_parsed[i], line_parsed[i] + line_parsed[i + 1] - 1)
            for i in range(0, len(line_parsed), 2)
        ]

        return seeds

    def parse_map(self, input: str):
        return [[[*map(int, i.split())] for i in j.split('\n')[1:]] for j in '\n'.join(input[2:]).split('\n\n')]

    def solve_part1(self):
        seed_location = []

        for seed in self.seeds_part1:
            for map in self.map_list:
                for dest, src, rng in map:
                    if src <= seed < src + rng:
                        idx = seed - src
                        seed = dest + idx
                        break

            seed_location.append(seed)

        return min(seed_location)

    def solve_part2(self):
        seed_locations = []
        
        for seed_pair in self.seeds_part2:
            heap = [seed_pair]
            res = []
            
            for map in self.map_list:
                while heap:
                    fst, lst = heap.pop()
                    
                    for dest, src, rng in map:
                        if lst < src or src + rng <= fst:
                            continue
                        elif src <= fst <= lst < src + rng:
                            offset = fst - src
                            res.append((dest + offset, dest + offset + lst - fst))
                            break
                        elif fst < src <= lst < src + rng:
                            offset = lst - src
                            res.append((dest, dest + offset))
                            heap.append((fst, src - 1))
                            break
                        elif src <= fst < src + rng <= lst:
                            offset = fst - src
                            res.append((dest + offset, dest + rng - 1))
                            heap.append((src + rng, lst))
                            break
                        elif fst < src <= src + rng <= lst:
                            res.append((dest, dest + rng - 1))
                            heap.append((fst, src - 1))
                            heap.append((src + rng, lst))
                            break
                    else:
                        res.append((fst, lst))
                
                heap = res
                res = []
            
            seed_locations.extend(heap)
        
        return min(fst for fst, lst in seed_locations)
