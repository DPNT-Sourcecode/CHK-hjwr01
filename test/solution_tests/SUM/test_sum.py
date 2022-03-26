from lib import solutions
# from solutions.SUM import sum_solution
import unittest

from .solutions.SUM import sum_solution

class TestSum(unittest.TestCase):
    def test_sum(self):
        res = sum_solution.compute(1, 2)
        self.assertEquals(res, 3)

if __name__ == "__main__":
    unittest.main()


