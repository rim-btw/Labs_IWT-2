import functools
from typing import Callable, Any

Tree = dict[str, Any]

def memoize(func: Callable) -> Callable:
    """
    Декоратор, кэширующий результаты функции.

    Ключ кэша строится из позиционных и именованных аргументов.
    Сохраняет метаданные исходной функции благодаря functools.wraps.
    Предоставляет методы cache_clear() и cache_info().
    """
    cache = {}
    hits = 0
    misses = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal hits, misses
        key = (args, tuple(sorted(kwargs.items())))
        
        if key in cache:
            hits += 1
            return cache[key]
        
        misses += 1
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    def cache_clear() -> None:
        """Очищает кэш и сбрасывает счетчики попаданий и промахов."""
        nonlocal cache, hits, misses
        cache.clear()
        hits = 0
        misses = 0

    def cache_info() -> str:
        """Возвращает строку со статистикой попаданий и промахов."""
        return f"CacheInfo(hits={hits}, misses={misses})"

    wrapper.cache_clear = cache_clear
    wrapper.cache_info = cache_info
    return wrapper

def gen_bin_tree_recursive(height: int = 6, root: int = 2) -> Tree:
    """
    Рекурсивно строит бинарное дерево (Вариант 2).
    
    Параметры:
        height (int): Высота дерева (по умолчанию 6).
        root (int): Значение корня (по умолчанию 2).

    Возвращает:
        Tree: Словарь, представляющий дерево.
    """
    if height <= 0:
        return {"value": root, "left": None, "right": None}
    
    left_val = root * 3
    right_val = root + 4
    
    return {
        "value": root,
        "left": gen_bin_tree_recursive(height - 1, left_val),
        "right": gen_bin_tree_recursive(height - 1, right_val)
    }

def gen_bin_tree_iterative(height: int = 6, root: int = 2) -> Tree:
    """
    Нерекурсивно строит бинарное дерево (Вариант 2).
    
    Параметры:
        height (int): Высота дерева (по умолчанию 6).
        root (int): Значение корня (по умолчанию 2).

    Возвращает:
        Tree: Словарь, представляющий дерево.
    """
    if height <= 0:
        return {"value": root, "left": None, "right": None}
    
    root_node = {"value": root, "left": None, "right": None}
    stack = [(root_node, 1)]
    
    while stack:
        node, current_height = stack.pop()
        
        if current_height <= height:
            left_val = node["value"] * 3
            right_val = node["value"] + 4
            
            left_child = {"value": left_val, "left": None, "right": None}
            right_child = {"value": right_val, "left": None, "right": None}
            
            node["left"] = left_child
            node["right"] = right_child
            
            stack.append((left_child, current_height + 1))
            stack.append((right_child, current_height + 1))
            
    return root_node

@memoize
def gen_bin_tree_recursive_memo(height: int = 6, root: int = 2) -> Tree:
    """
    Рекурсивная функция построения дерева, где рекурсивные вызовы проходят через кэш декоратора memoize.
    
    Параметры:
        height (int): Высота дерева (по умолчанию 6).
        root (int): Значение корня (по умолчанию 2).

    Возвращает:
        Tree: Словарь, представляющий дерево.
    """
    if height <= 0:
        return {"value": root, "left": None, "right": None}
    
    left_val = root * 3
    right_val = root + 4
    
    return {
        "value": root,
        "left": gen_bin_tree_recursive_memo(height - 1, left_val),
        "right": gen_bin_tree_recursive_memo(height - 1, right_val)
    }

def gen_bin_tree_iterative_memo(height: int = 6, root: int = 2) -> Tree:
    """
    Нерекурсивная функция построения дерева с внутренним кэшем.
    
    Кэш хранит поддеревья по ключу (значение_корня, высота_поддерева),
    что позволяет строить каждое уникальное поддерево только один раз.

    Параметры:
        height (int): Высота дерева (по умолчанию 6).
        root (int): Значение корня (по умолчанию 2).

    Возвращает:
        Tree: Словарь, представляющий дерево.
    """
    cache = {}
    
    def get_or_create(val: int, h: int) -> Tree:
        if h <= 0:
            return {"value": val, "left": None, "right": None}
        
        key = (val, h)
        if key in cache:
            return cache[key]
        
        node = {
            "value": val,
            "left": get_or_create(val * 3, h - 1),
            "right": get_or_create(val + 4, h - 1)
        }
        cache[key] = node
        return node

    return get_or_create(root, height)

@functools.lru_cache(maxsize=None)
def gen_bin_tree_recursive_lru(height: int = 6, root: int = 2) -> Tree:
    """
    Рекурсивная версия построения дерева с использованием стандартного functools.lru_cache.

    Параметры:
        height (int): Высота дерева (по умолчанию 6).
        root (int): Значение корня (по умолчанию 2).

    Возвращает:
        Tree: Словарь, представляющий дерево.
    """
    if height <= 0:
        return {"value": root, "left": None, "right": None}
    
    left_val = root * 3
    right_val = root + 4
    
    return {
        "value": root,
        "left": gen_bin_tree_recursive_lru(height - 1, left_val),
        "right": gen_bin_tree_recursive_lru(height - 1, right_val)
    }

def gen_bin_tree_recursive_v13(height: int = 3, root: int = 13) -> Tree:
    """
    Рекурсивная функция построения дерева для Варианта 13.
    
    Используется для сравнения в отчете.
    left_leaf = root + 1, right_leaf = root - 1.

    Параметры:
        height (int): Высота дерева (по умолчанию 3).
        root (int): Значение корня (по умолчанию 13).

    Возвращает:
        Tree: Словарь, представляющий дерево.
    """
    if height <= 0:
        return {"value": root, "left": None, "right": None}
    return {
        "value": root,
        "left": gen_bin_tree_recursive_v13(height - 1, root + 1),
        "right": gen_bin_tree_recursive_v13(height - 1, root - 1)
    }