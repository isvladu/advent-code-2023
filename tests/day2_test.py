import unittest
from solutions.day2 import Solution

class TestDay2(unittest.TestCase):
    def test_part1(self):
        solution = Solution(2, "test", 1)
        self.assertEqual(solution.solve_part1(), 8, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(2, "test", 2)
        self.assertEqual(solution.solve_part2(), 2286, "Part 2 is wrong.")

        