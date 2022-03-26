import unittest
from checkout_solution import checkout, cost_by_item_type


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

    # test helper function cost_by_item_type

    def test_cost_by_item_type(self):
        lookup = {1: 100, 3: 250, 5: 350}
        res = cost_by_item_type(10, lookup)
        self.assertEquals(res, 700)

    def test_cost_by_item_type_1(self):
        lookup = {1: 100, 3: 250, 5: 350}
        res = cost_by_item_type(2, lookup)
        self.assertEquals(res, 200)

    def test_cost_by_item_type_2(self):
        lookup = {1: 100, 3: 250, 5: 350}
        res = cost_by_item_type(4, lookup)
        self.assertEquals(res, 350)
        

if __name__ == '__main__':
    unittest.main()