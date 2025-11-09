def productExceptSelf(nums):
    result = [1] * len(nums)
    pre, post = 1, 1

    for i, num in enumerate(nums):
        result[i] = pre
        pre = num * pre

    for i in range(len(nums) - 1, -1, -1):
        result[i] *= post
        post *= nums[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))
