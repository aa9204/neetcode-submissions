class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if pairs.get(diff) != None:
                return [pairs.get(diff), i]
            pairs[nums[i]] = i
    

