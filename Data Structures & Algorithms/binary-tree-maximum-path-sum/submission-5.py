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
                return 0 # Setting it to 0 since now we don't compare subtree vals
                # with current node val. hence case where the tree = [-3] would pass.

            left_max = maxPath(node.left)
            right_max = maxPath(node.right)
            # We convert the negative values to 0 cause if may just want
            #  to return the node's value upwards cause negative value
            #  reduce the maximum so we can avoid them if we want
            left_max = max(0, left_max)
            right_max = max(0, right_max)

            self.max_path = max(self.max_path, node.val + left_max + right_max)
            
            return node.val + max(left_max, right_max)

        maxPath(root)
        return self.max_path

        # Time complexity: O(n)   Space complexity: O(n)

        
        