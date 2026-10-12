# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")
        
        def maxPath(node):    
            if not node:
                return float("-inf")

            left_max = maxPath(node.left)
            right_max = maxPath(node.right)

            paths= [
                left_max + node.val + right_max,
                left_max + node.val,
                right_max + node.val,
                node.val,
                left_max, 
                right_max
            ]

            max_val = max(paths)
            self.max_path = max(self.max_path, max_val)
            # print("max is set to: ", self.max_path)
            
            left_max = max(0, left_max)
            right_max = max(0, right_max)
            return node.val + max(left_max, right_max)

        maxPath(root)
        return self.max_path

        
        