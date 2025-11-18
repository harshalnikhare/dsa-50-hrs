def isAlienSorted(words, order):
    dict = {}

    for i, char in enumerate(order):
        dict[char] = i

    for i in range(len(words) - 1):

        found_difference = False
        curr_word = words[i]
        next_word = words[i + 1]

        for j in range(min(len(curr_word), len(next_word))):

            if dict[curr_word[j]] > dict[next_word[j]]:
                return False

            if dict[curr_word[j]] < dict[next_word[j]]:
                found_difference = True
                break

        if not found_difference and len(curr_word) > len(next_word):
            return False

    return True


print(isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))
print(isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
print(isAlienSorted(["z", "apple", "app"], "zabcdefghijklmnopqrstuvwxy"))
