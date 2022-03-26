import unittest
from hello_solution import hello


class TestHello(unittest.TestCase):

    def test_hello(self):
        res = hello("Alec")
        self.assertEquals(res, "Hello, World!")
    
    def test_hello_empty(self):
        res = hello("")
        self.assertEquals(res, "Hello, World!")

    def test_hello_wrong_type(self):
        with self.assertRaises(AssertionError):
            res = hello(None)


if __name__ == "__main__":
    unittest.main()
