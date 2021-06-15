# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.out = 0
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.out += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        dfs(root)
        return self.out