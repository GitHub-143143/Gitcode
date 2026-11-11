# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head == None:
            return head
        oe = []
        temp = head
        count = 1
        while temp:
            if count % 2 != 0:
                oe.append(temp.val)
            count += 1
            temp = temp.next
        temp = head.next
        while temp:
            oe.append(temp.val)
            if temp.next:
                temp = temp.next.next
            else:
                break
        link = ListNode(-1)
        oelink = link
        for i in oe:
            link.next = ListNode(i)
            link = link.next
        return oelink.next

        