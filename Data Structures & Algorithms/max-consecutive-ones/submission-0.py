class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            current = 0
            for j in range(i, len(nums)):
                if (nums[j] == 0):
                    break
                else:
                    current +=1
            count = max(current, count)
        return count
            

        