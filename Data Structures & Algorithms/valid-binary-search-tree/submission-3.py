# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validBST(node, lower_bound, upper_bound):
            if not node:
                return True
            
            if node.val >= upper_bound or node.val <= lower_bound:
                return False

            return validBST(node.left, lower_bound, node.val) and validBST(node.right, node.val, upper_bound)

        return validBST(root.left, float("-inf"), root.val) and validBST(root.right, root.val, float("inf"))
        # Time complexity: O(n)     Space complexity: O(h)