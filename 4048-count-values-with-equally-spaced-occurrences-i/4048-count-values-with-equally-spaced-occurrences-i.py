class Solution:
    def countSpecialIntegers(self, n: list[int]) -> int:
        count = 0
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                for k in range(j+1,len(n)):
                    if(n[i] == n[j] == n[k])and(j-i == k-j):
                        if n.count(n[i]) == 3:
                            count += 1
        return count