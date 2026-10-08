# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(node, k):
            nonlocal res
            if not node:
                return 

            inorder(node.left, k)
            res.append(node.val)
            inorder(node.right, k)
        
        inorder(root, k)
        return res[k-1]

        # Brute force solution cause we use a list and iterate it when returning the kth integer
        # Time complexity: O(n)     Space complexity: O(n)
