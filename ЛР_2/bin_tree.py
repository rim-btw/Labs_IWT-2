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


if __name__ == '__main__':
    import pprint
    tree = gen_bin_tree(height=2, root=2)
    print("Пример дерева (высота 2):")
    pprint.pprint(tree)