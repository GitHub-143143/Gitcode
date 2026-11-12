class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                s = nums[i:j+1]
                if s == sorted(s) and len(s)==len(set(s)):
                    a.append(nums[i:j+1])
                if s == sorted(s)[::-1] and len(s)==len(set(s)):
                    a.append(nums[i:j+1])
        if a: return max(len(x) for x in a)
        return 1
            