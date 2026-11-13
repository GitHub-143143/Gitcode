class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        dis = list()
        for i in arr:
            if arr.count(i)==1:
                dis.append(i)
        if len(dis) >= k:
            return dis[k-1]
        else:
            return ""
    
        