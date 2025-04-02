"""sliding window"""

def maximumLengthSubstring(s: str) -> int:
    l = 0
    r = 0
    _max = 1
    likeAset = {}

    likeAset[s[0]] = 1

    while r < len(s) - 1:
        r += 1
        if likeAset.get(s[r]): # se essa chave ja existe no dicionario
            likeAset[s[r]] += 1 # incremente
        else:
            likeAset[s[r]] = 1

        while likeAset[s[r]] == 3:
            likeAset[s[l]] -= 1
            l += 1
    
    _max = max(_max, r-l+1)

    return _max