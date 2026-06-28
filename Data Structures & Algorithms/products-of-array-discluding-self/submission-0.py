class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        z = 0
        for num in nums:
            if num is 0:
                z += 1
            else:
                product *= num
        if z > 1: return [0] * len(nums)
        ans = [0] * len(nums)
        for i, c in enumerate(nums):
            if z:
                ans[i] = 0 if c else product
            else:
                ans[i] = int(product / c)
        return ans


        