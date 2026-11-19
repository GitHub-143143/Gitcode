class Solution:
    def arrangeWords(self, text: str) -> str:
        a = text.lower().split()
        a.sort(key=len)
        a[0] = a[0].capitalize()
        return ' '.join(a)
        