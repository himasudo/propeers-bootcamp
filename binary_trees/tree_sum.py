
"""
**Tree Sum** — given the root of a binary tree, return the sum of all node values.

Same tree as before:

         1
      //   \\
     2       3
    // \\     \\
   4     5     6

Expected output: `1+2+3+4+5+6 = 21

Try writing `tree_sum(root)` using the same return-and-combine pattern as `count_nodes` — just swap what gets combined.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    return root.data + tree_sum(root.left) + tree_sum(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(f"sum of all the nodes in root is: {tree_sum(root)}")
