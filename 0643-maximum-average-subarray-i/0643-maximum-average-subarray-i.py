class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max = total
        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            if total > max:
                max = total
        return max/k