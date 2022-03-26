import unittest
from checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        res = checkout("ABCDCCC")
        self.assertEquals(res, 175)

    def test_checkout_empty(self):
        res = checkout("")
        self.assertEquals(res, 0)

    def test_checkout_wrong_format(self):
        with self.assertRaises(AssertionError):
            res = checkout([])

    def test_checkout_speacials(self):
        res = checkout("AAAABB")
        self.assertEquals(res, 225)

    def test_checkout_wrong_input(self):
        res = checkout("AAATTBB")
        self.assertEquals(res, -1)
        

if __name__ == '__main__':
    unittest.main()


