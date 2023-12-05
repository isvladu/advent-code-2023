import unittest
from solutions.day5 import Solution

class TestDay5(unittest.TestCase):
    def test_part1(self):
        solution = Solution(5, "test", 1)
        self.assertEqual(solution.solve_part1(), 35, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(5, "test", 2)
        self.assertEqual(solution.solve_part2(), 46, "Part 2 is wrong.")
