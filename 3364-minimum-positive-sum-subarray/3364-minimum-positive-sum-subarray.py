class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float('inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                n = nums[i:j+1]
                if len(n) >= l and len(n) <= r:
                    if sum(n) > 0:
                        mini = min(mini,sum(n))
        if mini == float('inf'): return -1
        return mini
        