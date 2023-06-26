class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        lrSum = 0
        for i in range(len(nums)-1):
            if (total - nums[i])/2 == sum(nums[i+1:]):
                return i
        if (total - nums[-1])/2 == sum(nums[:-1]):
            return len(nums)-1
        return -1
            
            