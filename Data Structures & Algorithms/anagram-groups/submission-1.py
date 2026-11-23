class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString not in answer:
                answer[sortedString] = []
            answer[sortedString].append(string)
        return list(answer.values())
            