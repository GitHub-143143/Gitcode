# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        rev = list()
        temp = head
        while temp:
            rev.append(temp.val)
            temp = temp.next
        while left <= right:
            rev[left-1:right] = rev[left-1:right][::-1]
            break
        dummy = ListNode(-1)
        ll = dummy
        for i in rev:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return ll.next
        
        