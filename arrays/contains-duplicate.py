def containsDuplicate(nums):
    hash_table = {}
    for i in range(len(nums)):
        if nums[i] in hash_table:
            return True
        else:
            hash_table[nums[i]] = True
    return False


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
