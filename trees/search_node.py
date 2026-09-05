"""
**Search a Node** — given the root of a binary tree and a `target` value, return `True` if `target` exists anywhere in the tree, `False` otherwise.

Same tree for reference:
```
         1
      //   \\
      2      3
    // \\     \\
   4    5      6
```
Examples: `search(root, 5)` → `True`, `search(root, 9)` → `False`

Try writing `search(root, target)` — same return-and-combine skeleton as before, but here you're combining with a boolean check instead of a sum/count. Think about what the base case should return when `root is None`, and how you'd combine the result of checking `root.data` with the results from left and right subtrees.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, target):
    if root is None:
        return False
    if root.data == target:
        return True
    return search(root.left, target) or search(root.right, target)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
n = 5
print(f"number {n} exists in tree: {search(root, n)}")