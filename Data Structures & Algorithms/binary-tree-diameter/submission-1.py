# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(root):
            if not root:
                return 0
            
            left_tree_len = dfs(root.left)
            right_tree_len = dfs(root.right)

            self.max_diameter = max(self.max_diameter, left_tree_len + right_tree_len)
            return 1 + max(left_tree_len, right_tree_len)

        dfs(root)
        return self.max_diameter