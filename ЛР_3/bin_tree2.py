from collections import deque
from typing import Optional, Callable, Dict, Union

TreeNode = Dict[str, Union[int, Optional['TreeNode']]]


def gen_bin_tree(
    height: int = 6,
    root: int = 2,
    left_leaf: Callable[[int], int] = lambda r: r * 3,
    right_leaf: Callable[[int], int] = lambda r: r + 4
) -> TreeNode:
    """
    Итеративно (нерекурсивно) строит бинарное дерево на основе заданных правил.

    Функция использует очередь для обхода в ширину (BFS).
    Это позволяет строить дерево уровень за уровнем без использования рекурсии.

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
    tree_root: TreeNode = {"value": root, "left": None, "right": None}
    
    if height <= 0:
        return tree_root

    queue = deque([(tree_root, 1)])

    while queue:
        current_node, current_level = queue.popleft()

        if current_level >= height:
            continue

        current_value = current_node["value"]

        left_value = left_leaf(current_value)
        right_value = right_leaf(current_value)

        left_node: TreeNode = {"value": left_value, "left": None, "right": None}
        right_node: TreeNode = {"value": right_value, "left": None, "right": None}

        current_node["left"] = left_node
        current_node["right"] = right_node

        queue.append((left_node, current_level + 1))
        queue.append((right_node, current_level + 1))

    return tree_root