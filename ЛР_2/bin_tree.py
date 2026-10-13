import unittest
from typing import Optional, Callable, Dict, Union

TreeNode = Dict[str, Union[int, Optional['TreeNode']]]

def gen_bin_tree(
    height: int = 6,
    root: int = 2,
    left_leaf: Callable[[int], int] = lambda r: r * 3,
    right_leaf: Callable[[int], int] = lambda r: r + 4
) -> TreeNode:
    """
    Рекурсивно строит бинарное дерево на основе заданных правил.

    Функция создает словарь, представляющий узел дерева. Если высота (height) больше 0,
    рекурсивно создаются левое и правое поддеревья с использованием функций left_leaf и right_leaf
    для вычисления значений потомков.

    Аргументы:
        height (int): Высота дерева (количество уровней). По умолчанию 6.
        root (int): Значение корневого узла. По умолчанию 2.
        left_leaf (Callable[[int], int]): Функция для вычисления значения левого потомка.
                                          По умолчанию: lambda r: r * 3.
        right_leaf (Callable[[int], int]): Функция для вычисления значения правого потомка.
                                           По умолчанию: lambda r: r + 4.

    Возвращает:
        TreeNode: Словарь с ключами 'value', 'left', 'right'.
    """
    if height <= 0:
        return {
            "value": root,
            "left": None,
            "right": None
        }
    return {
        "value": root,
        "left": gen_bin_tree(
            height=height - 1,
            root=left_leaf(root),
            left_leaf=left_leaf,
            right_leaf=right_leaf
        ),
        "right": gen_bin_tree(
            height=height - 1,
            root=right_leaf(root),
            left_leaf=left_leaf,
            right_leaf=right_leaf
        )
    }

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
        current = tree
        for _ in range(6):
            current = current['left']
        self.assertIsNotNone(current)
        self.assertIsNone(current['left'])
        self.assertIsNone(current['right'])

    def test_custom_functions(self):
        """Проверка работы с пользовательскими лямбда-функциями."""
        tree = gen_bin_tree(
            height=2,
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