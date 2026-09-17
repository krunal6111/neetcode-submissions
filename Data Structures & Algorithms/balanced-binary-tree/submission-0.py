# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def isHeightBalanced(root):
            if not root:
                return 0, True # height, Balanced Flag

            l_height, l_bal = isHeightBalanced(root.left)
            r_height, r_bal = isHeightBalanced(root.right)

            if not l_bal or not r_bal:
                return 0, False

            return (1 + max(l_height, r_height), True) if abs(l_height - r_height) <= 1 else (0, False)

        _, flag = isHeightBalanced(root)

        return flag