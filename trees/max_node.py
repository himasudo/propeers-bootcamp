"""
**Find Max** — given the root of a binary tree, return the maximum value among all node values in the tree.

Same tree for reference:
```
        1
      //   \\
      2     3
    // \\    \\
   4    5     6
```
Expected output: `6`

Try writing `find_max(root)` using the same return-and-combine recursive pattern — think about what you compare and combine at each node instead of what you sum or count.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_max(root):
    if root is None:
        return float("-inf")
    return max(root.data, find_max(root.left), find_max(root.right))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(f"max of all the nodes in root is: {find_max(root)}")