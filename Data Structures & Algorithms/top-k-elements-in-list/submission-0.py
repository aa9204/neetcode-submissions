class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num,0) + 1
        sorted_res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        keys = list(sorted_res.keys())
        return keys[0:k]
        

        
