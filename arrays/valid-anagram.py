def isAnagram(s, t):
    look_up = {}
    for char in s:
        if char in look_up:
            look_up[char] += 1
        else:
            look_up[char] = 1

    for char in t:
        if char in look_up:
            if look_up[char] == 1:
                del look_up[char]
            else:
                look_up[char] -= 1
        else:
            return False

    return len(look_up) == 0


# anagram with array of english letters
def isAnagram2(s, t):
    if len(s) != len(t):
        return False

    arr = [0] * 26

    for i in range(len(s)):
        arr[ord(s[i]) - 97] += 1
        arr[ord(t[i]) - 97] -= 1

    for val in arr:
        if val != 0:
            return False

    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
