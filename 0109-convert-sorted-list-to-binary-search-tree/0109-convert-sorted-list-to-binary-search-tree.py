# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        nums = list()
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        def solve(nums):
            if not nums: return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = solve(nums[:mid])
            root.right = solve(nums[mid+1:])
            return root
        return solve(nums)

        