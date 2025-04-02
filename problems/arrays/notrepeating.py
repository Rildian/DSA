def longestWithoutRepeating(s: str) -> int:
    charSet = set()

    l = 0
    r = 0
    result = 0

    while r < len(s):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        result = max(result, r-l+1)
        r += 1
    
    return result


string = "bcbbbcba"

print(longestWithoutRepeating(string))