import unittest
from solutions.day3 import Solution

class TestDay3(unittest.TestCase):
    def test_part1(self):
        solution = Solution(3, "test", 1)
        self.assertEqual(solution.solve_part1(), None, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(3, "test", 2)
        self.assertEqual(solution.solve_part2(), None, "Part 2 is wrong.")
