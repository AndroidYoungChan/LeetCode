class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        total = 0
        for i in range(len(gain)):
            altitudes.append(gain[i]+altitudes[-1])
        return max(altitudes)
            