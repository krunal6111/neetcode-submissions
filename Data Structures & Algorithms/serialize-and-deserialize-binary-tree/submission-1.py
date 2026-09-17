# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # DFS
        # res = []
        # def dfs(root):
        #     if not root:
        #         res.append("N")
        #         return None

        #     res.append(str(root.val))
        #     dfs(root.left)
        #     dfs(root.right)

        # dfs(root)
        # return ",".join(res)

        # BFS
        if not root:
            return "N"

        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        print(res, "RES in serialize")
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # DFS
        # val = data.split(',')
        # if val[0] == "N":
        #     return None
        
        # self.i = 0
        # def dfs():
        #     if val[self.i] == "N":
        #         self.i += 1 
        #         return None
            
        #     node = TreeNode(int(val[self.i]))
        #     self.i += 1
        #     node.left = dfs()
        #     node.right = dfs()
                
        #     return node
        
        # return dfs()

        # BFS
        vals = data.split(",")
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1

        return root
            
