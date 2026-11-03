class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        a = len(nums)//2
        moves = 0
        for i in range(len(nums)):
            moves += abs(nums[a]-nums[i])
        return moves
        