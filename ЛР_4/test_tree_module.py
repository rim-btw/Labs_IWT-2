import unittest
from tree_module import (
    gen_bin_tree_recursive, 
    gen_bin_tree_iterative, 
    gen_bin_tree_recursive_memo, 
    gen_bin_tree_iterative_memo,
    memoize
)

class TestBinTree(unittest.TestCase):
    """
    Тесты для проверки корректности построения деревьев и работы декоратора memoize.
    """
    
    def test_memoized_equals_regular(self):
        """Проверяет, что мемоизированные версии строят то же дерево, что и обычные."""
        h, r = 4, 2
        tree_reg_rec = gen_bin_tree_recursive(h, r)
        tree_reg_iter = gen_bin_tree_iterative(h, r)
        tree_memo_rec = gen_bin_tree_recursive_memo(h, r)
        tree_memo_iter = gen_bin_tree_iterative_memo(h, r)
        
        self.assertEqual(tree_reg_rec, tree_memo_rec)
        self.assertEqual(tree_reg_rec, tree_memo_iter)
        self.assertEqual(tree_reg_iter, tree_memo_rec)

    def test_memoize_decorator_does_not_call_func_twice(self):
        """Проверяет, что декоратор memoize не вызывает функцию повторно для тех же аргументов."""
        call_count = 0
        
        @memoize
        def dummy_func(x):
            nonlocal call_count
            call_count += 1
            return x * 2
            
        dummy_func(5)
        dummy_func(5)
        dummy_func(10)
        
        self.assertEqual(call_count, 2)
        
    def test_memoize_kwargs(self):
        """Проверяет, что вызовы с именованными аргументами не приводят к ошибке и кэшируются корректно."""
        @memoize
        def dummy_func(a, b=2):
            return a + b
            
        self.assertEqual(dummy_func(1, b=3), 4)
        self.assertEqual(dummy_func(a=1, b=3), 4)
        self.assertEqual(dummy_func(1, 3), 4)
        
    def test_shared_subtrees_are_same_object(self):
        """Проверяет, что одинаковые поддеревья в мемоизированном дереве являются одним объектом в памяти."""
        tree = gen_bin_tree_recursive_memo(height=2, root=2)
        
        self.assertIs(tree["left"], tree["right"])
        
        tree["left"]["value"] = 999
        self.assertEqual(tree["right"]["value"], 999)

if __name__ == '__main__':
    unittest.main()