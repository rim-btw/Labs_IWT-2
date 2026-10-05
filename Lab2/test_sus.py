import unittest
from sus import add

class AddTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add([2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(add([3, 2, 4], 6), [1, 2])

    def test_3(self):
        self.assertEqual(add([3, 3], 6), [0, 1])

if __name__ == '__main__':
    unittest.main()