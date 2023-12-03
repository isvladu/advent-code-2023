import unittest
from solutions.day1 import Solution

class TestDay1(unittest.TestCase):
    def test_part1(self):
        solution = Solution(1, "test", 1)
        self.assertEqual(solution.solve_part1(), 142, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(1, "test", 2)
        self.assertEqual(solution.solve_part2(), 281, "Part 2 is wrong.")
