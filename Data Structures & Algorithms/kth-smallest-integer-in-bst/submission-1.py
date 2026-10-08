# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        count = 0
        def inorder(node, k):
            nonlocal count, res
            if not node:
                return 

            inorder(node.left, k)
            count += 1
            if count == k:
                res = node.val
                return 

            inorder(node.right, k)
        
        inorder(root, k)
        return res

        # Brute force solution cause we use a list and iterate it when returning the kth
        # Time complexity: O(n)     Space complexity: O(n)
