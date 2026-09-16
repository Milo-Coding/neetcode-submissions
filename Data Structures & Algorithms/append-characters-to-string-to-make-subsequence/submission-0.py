class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sliced = s
        i = 0
        while len(sliced) != 0 and i < len(t): # letters in s to consider
            if t[i] == sliced[0]:
                sliced = sliced[1:]
                i += 1
                continue
            else:
                sliced = sliced[1:]
        return len(t) - i