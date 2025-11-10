roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s):
    total = 0

    i = len(s) - 1
    while i >= 1:
        val = roman_dict[s[i]]
        prevVal = roman_dict[s[i - 1]]

        if val > prevVal:
            total += val - prevVal
            i -= 2
        else:
            total += val
            i -= 1
    total += roman_dict[s[0]]

    return total


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
