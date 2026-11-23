def add(nums, target):
    """Возвращает индексы двух разных элементов, сумма которых равна target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None