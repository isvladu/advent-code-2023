import unittest
from solutions.day6 import Solution

class TestDay6(unittest.TestCase):
    def test_part1(self):
        solution = Solution(6, "test", 1)
        self.assertEqual(solution.solve_part1(), 288, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(6, "test", 2)
        self.assertEqual(solution.solve_part2(), 71503, "Part 2 is wrong.")
