import unittest
from solutions.day8 import Solution

class TestDay8(unittest.TestCase):
    def test_part1(self):
        solution = Solution(8, "test", 1)
        self.assertEqual(solution.solve_part1(), 2, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(8, "test", 2)
        self.assertEqual(solution.solve_part2(), 6, "Part 2 is wrong.")
