import unittest
from solutions.day7 import Solution

class TestDay7(unittest.TestCase):
    def test_part1(self):
        solution = Solution(7, "test", 1)
        self.assertEqual(solution.solve_part1(), 6440, "Part 1 is wrong.")
        
    def test_part2(self):
        solution = Solution(7, "test", 2)
        self.assertEqual(solution.solve_part2(), 5905, "Part 2 is wrong.")
