# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        queue = [root]

        while queue: 
            level = []
            # The loop will iterate only that many times how much it's length is measure at 1st iteration. 
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node:
                    continue
                
                # Add the next level's nodes to the queue
                queue.append(node.left)
                queue.append(node.right)

                # Add the current node to it's respective level
                level.append(node.val)

            if len(level) != 0:
                res.append(level[-1])
            else:
                break
        
        return res

        # Time complexity: O(n) Space complexity: O(n)