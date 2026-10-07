# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_val = float("-inf")
        good_nodes = 0

        def dfs(root, max_val):
            nonlocal good_nodes
            if not root:
                return
            
            max_val = max(max_val, root.val)
            if root.val >= max_val:
                good_nodes += 1
            
            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, max_val)
        return good_nodes

        # Time complexity: O(n)     Space complexity: O(1)



        