class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resultS = {}
        resultT = {}
        if len(s) != len(t):
            return False
        for char in s:
            resultS[char] = resultS.get(char, 0) + 1
        for char in t:
            resultT[char] = resultT.get(char, 0) + 1
        return resultS == resultT
        