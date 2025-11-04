def group_anagram(arr):

    if len(arr) == 0:
        return []

    hash_map = {}

    for str in arr:
        alphTable = [0] * 26

        for char in str:
            alphTable[ord(char) - 97] += 1

        alphStr = tuple(alphTable)

        if alphStr not in hash_map:
            hash_map[alphStr] = [str]
        else:
            hash_map[alphStr].append(str)

    return list(hash_map.values())


print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagram([""]))
print(group_anagram(["a"]))
