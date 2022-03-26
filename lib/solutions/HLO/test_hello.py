import unittest
from hello_solution import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        res = hello("")
        self.assertEquals(res, "Hello to ")


if __name__ == "__main__":
    unittest.main()

