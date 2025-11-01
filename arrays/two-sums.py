from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            return [hash_map[target - nums[i]], i]
        else:
            hash_map[nums[i]] = i
    return [-1, -1]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
