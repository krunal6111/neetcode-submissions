# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []

        def dfs(root):
            if not root:
                self.res.append("N")
                return

            self.res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        string = ",".join(self.res)
        print(string)
        return string

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.preorder = data.split(',')
        self.i = 0

        def dfs():
            if self.i == len(self.preorder) - 1 or self.preorder[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(self.preorder[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


