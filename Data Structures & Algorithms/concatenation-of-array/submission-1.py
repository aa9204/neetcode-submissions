class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = 2 * len(nums)
        n = len(nums)
        ans = [0] * length
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans

        