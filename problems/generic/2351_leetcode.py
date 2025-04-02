class Solution(object):
    def repeatedCharacter(self, s):
        seen = set()

        for letter in s:
            if letter in seen:
                return letter
            seen.add(letter)
