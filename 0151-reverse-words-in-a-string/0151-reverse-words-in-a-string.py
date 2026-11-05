class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.split()
        low = 0
        high = len(r)-1
        while low <=high:
            r[low],r[high] = r[high],r[low]
            low += 1
            high -= 1
        return ' '.join(r)        