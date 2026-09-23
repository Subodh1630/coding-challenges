def contains_duplicate(nums: list[int]) -> bool:
    seen = set(nums)
    if len(nums) > len(seen):
        return True
    else: return False


print(contains_duplicate([1, 2, 3, 1]))   # True
print(contains_duplicate([1, 2, 3, 4]))   # False
print(contains_duplicate([]))             # False
print(contains_duplicate([1]))            # False
print(contains_duplicate([0, 0]))         # True
print(contains_duplicate([-1, 0, -1]))    # True