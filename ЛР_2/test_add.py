import unittest
from add import add


class TestAdd(unittest.TestCase):
    """
    Набор тестов для функции add(nums, target).
    Проверяет различные группы ситуаций и крайние случаи.
    """

    def test_basic_case(self):
        result = add([2, 7, 11, 15], 9)
        self.assertIn(result, ([0, 1], [1, 0]))

    def test_pair_at_the_end(self):
        result = add([1, 2, 3, 4, 5, 6], 11)  # 5 + 6 = 11
        self.assertIn(result, ([4, 5], [5, 4]))

    def test_negative_numbers(self):
        result = add([-3, 4, 3, 90], 0)  # -3 + 3 = 0
        self.assertIn(result, ([0, 2], [2, 0]))

    def test_duplicate_numbers(self):
        result = add([3, 3], 6)
        self.assertIn(result, ([0, 1], [1, 0]))

    def test_negative_target(self):
        result = add([-1, -2, -3, -4, -5], -8)  # -3 + -5 = -8
        self.assertIn(result, ([2, 4], [4, 2]))

    def test_no_solution(self):
        result = add([1, 2, 3, 4], 100)
        self.assertIsNone(result)

    def test_empty_list(self):
        result = add([], 5)
        self.assertIsNone(result)

    def test_single_element(self):
        result = add([5], 10)
        self.assertIsNone(result)

    def test_zeros(self):
        result = add([0, 4, 0], 0)
        self.assertIn(result, ([0, 2], [2, 0]))


if __name__ == "__main__":
    unittest.main()