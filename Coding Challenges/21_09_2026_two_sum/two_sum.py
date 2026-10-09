def two_sum(nums: List[int], target: int) -> tuple[int, int] | None:
    for index1 in range(len(nums)):
        for index2 in range(index1 + 1, len(nums)):
            if nums[index1] + nums[index2] == target:
                return (index1, index2)

print(two_sum([2, 7, 11, 15], 9))  # (0, 1)
print(two_sum([3, 3], 6))  # (0, 1)
print(two_sum([3], 6))  # None
print(two_sum([2, 5, 5, 11], 10))  # (1, 2)
print(two_sum([-3, 4, 3, 90], 0))  # (0, 2)
print(two_sum([1, 2, 3], 20))  # None