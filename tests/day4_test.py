import unittest
from solutions.day4 import Solution

class TestDay4(unittest.TestCase):
    def test_part1(self):
        solution = Solution(4, "test", 1)
        self.assertEqual(solution.solve_part1(), 13, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(4, "test", 2)
        self.assertEqual(solution.solve_part2(), 30, "Part 2 is wrong.")
