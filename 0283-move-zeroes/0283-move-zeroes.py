import copy

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        for i in nums:
            if i != 0:
                ans.append(i)
        for i in range(len(nums)-len(ans)):
            ans.append(0);
        
        for i in range(len(ans)):
            nums[i] = ans[i]