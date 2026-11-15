class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd , even = 0 , 1
        total , count = 0 , 0
        for i in arr:
            total += i
            if total % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1
        return count % (10**9 + 7)  