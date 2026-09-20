def two_sum(nums: List[int], target: int) -> tuple[int, int] | None:
    seen = {}

    for current_index, current_number in enumerate(nums):
        required_number = target - current_number

        if required_number in seen:
            return seen[required_number], current_index
        seen[current_number] = current_index

    return None

print(two_sum([2, 7, 11, 15], 9))  # (0, 1)
print(two_sum([3, 3], 6))  # (0, 1)
print(two_sum([3], 6))  # None
print(two_sum([2, 5, 5, 11], 10))  # (1, 2)
print(two_sum([-3, 4, 3, 90], 0))  # (0, 2)
print(two_sum([1, 2, 3], 20))  # None
