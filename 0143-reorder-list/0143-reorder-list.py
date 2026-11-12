# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        reorder = list()
        temp = head
        while temp:
            reorder.append(temp.val)
            temp = temp.next
        low , high = 0 , len(reorder)-1
        temp = head
        while low <=high:
            if low != high:
                temp.val = reorder[low]
                temp.next.val = reorder[high]
                temp = temp.next.next
            else:
                temp.val = reorder[low]
                break
            low += 1
            high -= 1
        
        
        


        