class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans = {}
        for i in arr:
            ans[i] = 0
        for i in arr:
            ans[i] +=1
        k = list(ans.values())
        if len(k) != len(set(k)):
            return False
        return True
            