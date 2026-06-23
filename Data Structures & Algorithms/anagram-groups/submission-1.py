class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            for char in word:
                alpha[ord(char) - ord('a')] += 1
            ans[tuple(alpha)].append(word)
        return list(ans.values())
        