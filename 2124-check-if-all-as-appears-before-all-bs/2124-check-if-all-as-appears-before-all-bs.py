class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=sorted(s)
        a="".join(a)
        return a==s
        