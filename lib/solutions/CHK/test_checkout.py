import unittest
from checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        res = checkout("A B C D C C C")
        self.assertEquals(res, 175)

    def test_checkout_empty(self):
        res = checkout("")
        self.assertEquals(res, 0)

    def test_checkout_wrong_format(self):
        with self.assertRaises(AssertionError):
            res = checkout([])
        

