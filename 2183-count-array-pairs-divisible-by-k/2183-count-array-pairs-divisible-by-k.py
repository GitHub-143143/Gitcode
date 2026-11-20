class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        from math import gcd
        count = 0
        d = {}
        for i in nums:
            g = gcd(i,k)
            for j in d:
                if (g*j) % k == 0:
                    count += d[j]
            d[g] = d.get(g,0)+1
        return count
        