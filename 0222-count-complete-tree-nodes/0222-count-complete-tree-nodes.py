# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if root == None: return 0
        left = right = root
        l = r = 0
        while left:
            l += 1
            left = left.left
        while right:
            r += 1
            right = right.right
        if l == r:
            return (2 ** l) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        