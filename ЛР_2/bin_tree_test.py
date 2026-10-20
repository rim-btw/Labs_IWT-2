import unittest
from bin_tree import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    """
    Тесты для проверки функции gen_bin_tree.
    """

    def test_default_values(self):
        """Проверка работы с параметрами по умолчанию (Вариант 2)."""
        tree = gen_bin_tree()
        self.assertEqual(tree['value'], 2)
        self.assertEqual(tree['left']['value'], 6)
        self.assertEqual(tree['right']['value'], 6)
        
        # ИСПРАВЛЕНО: height=6, значит нужно сделать 6 спусков, чтобы дойти до листа
        current = tree
        for _ in range(6):
            current = current['left']
        self.assertIsNotNone(current)
        self.assertIsNone(current['left'])
        self.assertIsNone(current['right'])

    def test_custom_functions(self):
        """Проверка работы с пользовательскими лямбда-функциями."""
        tree = gen_bin_tree(
            height=3,
            root=10,
            left_leaf=lambda r: r - 5,
            right_leaf=lambda r: r * 10
        )
        self.assertEqual(tree['value'], 10)
        self.assertEqual(tree['left']['value'], 5)
        self.assertEqual(tree['right']['value'], 100)
        self.assertEqual(tree['left']['left']['value'], 0)
        self.assertEqual(tree['right']['right']['value'], 1000)

    def test_zero_height(self):
        """Проверка граничного случая: высота 0."""
        tree = gen_bin_tree(height=0, root=99)
        self.assertEqual(tree['value'], 99)
        self.assertIsNone(tree['left'])
        self.assertIsNone(tree['right'])

    def test_negative_height(self):
        """Проверка граничного случая: отрицательная высота."""
        tree = gen_bin_tree(height=-1, root=50)
        self.assertEqual(tree['value'], 50)
        self.assertIsNone(tree['left'])
        self.assertIsNone(tree['right'])


if __name__ == '__main__':
    unittest.main()