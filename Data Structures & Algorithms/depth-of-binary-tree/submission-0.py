# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        def max_depth(root, count):
            if not root:
                return count

            count += 1
            count_left = max_depth(root.left, count)
            count_right = max_depth(root.right, count)
            return max(count_left, count_right)

        return max_depth(root, count)