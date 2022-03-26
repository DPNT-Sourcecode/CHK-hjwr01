import unittest
import sum_solution

# Having problems with with python finding the solutions library... Doing testing here to save time

class TestSum(unittest.TestCase):
    def test_sum(self):
        res = sum_solution.compute(1, 2)
        self.assertEquals(res, 3)

    def test_sum_incorrect(self):
        res = sum_solution.compute(10, 2)
        self.assertNotEquals(res, 5)

    def test_sum_negative(self):
        with self.assertRaises(AssertionError):
            res = sum_solution.compute(-5, 2)

if __name__ == "__main__":
    unittest.main()
