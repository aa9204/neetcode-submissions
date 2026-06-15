class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r = len(arr) - 1
        max = -1
        temp = 0
        for i in range(len(arr)):
            temp = arr[r]
            arr[r] = max
            if (temp > max): 
                max = temp
            r -= 1
        return arr



        