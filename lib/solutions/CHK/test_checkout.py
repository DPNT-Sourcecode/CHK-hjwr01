import unittest
from checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        res = checkout("A B C D C C C")
