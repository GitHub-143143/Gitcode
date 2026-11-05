class Solution:
    def reverseWords(self, s: str) -> str:
        rev = s.split()
        low = 0
        high = len(rev)-1
        while low <=high:
            rev[low],rev[high] = rev[high],rev[low]
            low += 1
            high -= 1
        return " ".join(rev)[::-1]

              