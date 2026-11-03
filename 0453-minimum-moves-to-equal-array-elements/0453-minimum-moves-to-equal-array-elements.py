class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        sums = 0
        for i in nums:
            sums += abs(mini-i)
        return sums
        