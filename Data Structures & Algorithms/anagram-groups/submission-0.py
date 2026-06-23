class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for word in strs:
            sort_word = "".join(sorted(word))
            maps[sort_word].append(word)
        return(list(maps.values()))
            



        