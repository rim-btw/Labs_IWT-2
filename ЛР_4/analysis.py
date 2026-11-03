import timeit
import functools
import matplotlib.pyplot as plt
from tree_module import (
    gen_bin_tree_recursive, gen_bin_tree_iterative,
    gen_bin_tree_recursive_memo, gen_bin_tree_iterative_memo,
    gen_bin_tree_recursive_lru, gen_bin_tree_recursive_v13
)

heights = [2, 4, 6, 8, 10, 12, 14, 16]
number_of_runs = 100

results = {
    "Var2_Recursive": [], "Var2_Iterative": [],
    "Var2_Recursive_Memo": [], "Var2_Iterative_Memo": [],
    "Var2_Recursive_LRU": [],
    "Var13_Recursive": [], "Var13_Recursive_Memo": []
}

for h in heights:
    gen_bin_tree_recursive_memo.cache_clear()
    gen_bin_tree_recursive_lru.cache_clear()
    
    t_rec = timeit.timeit(lambda: gen_bin_tree_recursive(h, 2), number=number_of_runs) / number_of_runs
    t_iter = timeit.timeit(lambda: gen_bin_tree_iterative(h, 2), number=number_of_runs) / number_of_runs
    
    def run_memo_rec():
        gen_bin_tree_recursive_memo.cache_clear()
        return gen_bin_tree_recursive_memo(h, 2)
    
    def run_memo_lru():
        gen_bin_tree_recursive_lru.cache_clear()
        return gen_bin_tree_recursive_lru(h, 2)
        
    t_memo_rec = timeit.timeit(run_memo_rec, number=number_of_runs) / number_of_runs
    t_memo_iter = timeit.timeit(lambda: gen_bin_tree_iterative_memo(h, 2), number=number_of_runs) / number_of_runs
    t_lru = timeit.timeit(run_memo_lru, number=number_of_runs) / number_of_runs
    
    results["Var2_Recursive"].append(t_rec)
    results["Var2_Iterative"].append(t_iter)
    results["Var2_Recursive_Memo"].append(t_memo_rec)
    results["Var2_Iterative_Memo"].append(t_memo_iter)
    results["Var2_Recursive_LRU"].append(t_lru)

    t_v13_rec = timeit.timeit(lambda: gen_bin_tree_recursive_v13(h, 13), number=number_of_runs) / number_of_runs
    results["Var13_Recursive"].append(t_v13_rec)
    
    @functools.lru_cache(maxsize=None)
    def gen_v13_memo(h: int, r: int):
        if h <= 0: return {"value": r, "left": None, "right": None}
        return {"value": r, "left": gen_v13_memo(h-1, r+1), "right": gen_v13_memo(h-1, r-1)}
    
    t_v13_memo = timeit.timeit(lambda: (gen_v13_memo.cache_clear(), gen_v13_memo(h, 13))[1], number=number_of_runs) / number_of_runs
    results["Var13_Recursive_Memo"].append(t_v13_memo)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

for label, times in results.items():
    if label.startswith("Var2"):
        ax1.plot(heights, times, marker='o', label=label)
ax1.set_title("Вариант 2: Сравнение времени (Одно построение)")
ax1.set_xlabel("Высота дерева (height)")
ax1.set_ylabel("Время (сек)")
ax1.legend()
ax1.grid(True)

ax2.plot(heights, results["Var13_Recursive"], marker='o', label="Var13_Recursive")
ax2.plot(heights, results["Var13_Recursive_Memo"], marker='o', label="Var13_Recursive_Memo")
ax2.set_title("Вариант 13: Сравнение времени (Одно построение)")
ax2.set_xlabel("Высота дерева (height)")
ax2.set_ylabel("Время (сек)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig("graphs.png")