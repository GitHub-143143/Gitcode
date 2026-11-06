# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1 , temp2 = list1 ,list2
        list3 , list4 = list() , list()
        merge = []
        while temp1:
            list3.append(temp1.val)
            temp1 = temp1.next
        while temp2:
            list4.append(temp2.val)
            temp2 = temp2.next
        for i in range(a):
            merge.append(list3[i])
        merge = merge + list4
        merge = merge + list3[b+1:]
        dummy = ListNode(-1)
        temp = dummy
        for i in range(len(merge)):
            dummy.next = ListNode(merge[i])
            dummy = dummy.next
        return temp.next
        

        