# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        nodes = []
        temp = head
        while temp:
            nodes.append(temp.val)
            temp = temp.next
        sums = 0
        merge = ListNode(-1)
        dummy = merge
        for i in nodes:
            if i!= 0:
                sums+= i
            else:
                merge.next = ListNode(sums)
                merge = merge.next
                sums = 0
        return dummy.next.next