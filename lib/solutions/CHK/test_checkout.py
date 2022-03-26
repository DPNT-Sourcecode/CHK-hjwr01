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

    @unittest.skip("no longer relevant")
    def test_checkout_wrong_input(self):
        res = checkout("AAATTBB")
        self.assertEquals(res, -1)

    def test_checkout_new_E_offer(self):
        res = checkout("AEEBB")
        self.assertEquals(res, 160)

    def test_checkout_new_F_offer(self):
        res = checkout("FFF")
        self.assertEquals(res, 20)

    def test_checkout_F_offer_low_F(self):
        res = checkout("FF")
        self.assertEquals(res, 20)

    def test_checkout_F_offer_8_F(self):
        res = checkout("FFFFFFFF")
        self.assertEquals(res, 60)

    def test_U(self):
        res = checkout("UUUU")
        self.assertEquals(res, 120)
    
    def test_U_1(self):
        res = checkout("UUUUU")
        self.assertEquals(res, 160)

    def test_U_2(self):
        res = checkout("UUUUUUUU")
        self.assertEquals(res, 240)

    def test_R(self):
        res = checkout("RRRQ")
        self.assertEquals(res, 150)
    
    def test_R_1(self):
        res = checkout("RRRQQ")
        self.assertEquals(res, 180)
    
    def test_R_2(self):
        res = checkout("RRRRQ")
        self.assertEquals(res, 200)

    def test_xyzst(self):
        res = checkout("XYZ")
        self.assertEquals(res, 45)

    def test_xyzst(self):
        res = checkout("XYZZZ")
        self.assertEquals(res, 82)
        

if __name__ == '__main__':
    unittest.main()
