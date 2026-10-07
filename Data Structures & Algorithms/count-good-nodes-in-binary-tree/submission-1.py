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

        def dfs(node, max_val):
            if not node:
                return 0
            
            max_val = max(max_val, node.val)
            good_node = node.val >= max_val
            
            return (
                good_node +
                dfs(node.left, max_val) + 
                dfs(node.right, max_val)
            )
        
        return dfs(root, max_val)

        # Time complexity: O(n)     Space complexity: O(h) recursive space



        