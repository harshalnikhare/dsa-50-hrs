# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


# Approach 1
def containsNearbyDuplicate(nums, k):
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map and abs(hash_map[nums[i]] - i) <= k:
            return True
        else:
            hash_map[nums[i]] = i
    return False


# Approach 2 maintaining a window technique
def containsNearbyDuplicate2(nums, k):
    hash_set = set()
    for i, num in enumerate(nums):
        if num in hash_set:
            return True
        hash_set.add(num)
        if len(hash_set) > k:
            hash_set.remove(nums[i - k])

    return False
