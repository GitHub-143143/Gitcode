# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        Nodes = []
        temp = head
        while temp:
            Nodes.append(temp.val)
            temp = temp.next
        a , b = k , 0
        for i in range(len(Nodes)):
            if len(Nodes[b:a]) >= k:
                Nodes[b:a] = Nodes[b:a][::-1]
            b += k
            a += k
        group = ListNode(Nodes[0])
        link = group
        for i in range(1,len(Nodes)):
            group.next = ListNode(Nodes[i])
            group = group.next
        return link