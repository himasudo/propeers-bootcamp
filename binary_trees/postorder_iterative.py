"""
**Iterative Postorder** — write `postorder_iterative(root)` that returns/prints node values in postorder (left → right → root), but *without recursion* — using explicit stack(s) instead.

Same tree for reference:
```
        1
      //   \\
      2     3
    // \\    \\
   4    5      6
```
Expected output: `4 5 2 6 3 1`

Heads up on difficulty (as the instructor flagged): unlike iterative preorder — where a single stack with "push right then left" was a clean trick — postorder is harder because the root needs to be processed **last**, not first. A single stack alone won't cleanly give you that ordering. The instructor said this typically needs **two stacks**.

Hint to get you started, without giving the solution: think about what you'd get if you did a *modified preorder* — root → **right** → left (i.e., swap the push order from what you did last time) — and collected results into a second stack instead of printing immediately. What order would popping that second stack give you?

Go ahead and attempt it.
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder_iterative(root):
    if root is None:
        return
    node_stack = [root]
    data_stack = []
    while node_stack:
        node = node_stack.pop()
        if node.left:
            node_stack.append(node.left)
        if node.right:
            node_stack.append(node.right)
        data_stack.append(node.data)

    while(data_stack):
        num = data_stack.pop()
        print(num)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("post-order tree traversal:")
postorder_iterative(root)