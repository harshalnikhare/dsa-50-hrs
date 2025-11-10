import heapq


def topKFrequent(nums, k):
    if k == len(nums):
        return nums

    freq_counter = {}
    for num in nums:
        if num in freq_counter:
            freq_counter[num] += 1
        else:
            freq_counter[num] = 1

    pq = []

    for key, freq in freq_counter.items():
        heapq.heappush(pq, (freq, key))
        if len(pq) > k:
            heapq.heappop(pq)

    return [key for freq, key in pq]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
