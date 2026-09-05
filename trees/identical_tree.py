"""
**Same Tree / Identical Trees** — given the roots of two binary trees, `p` and `q`, return `True` if they are structurally identical *and* all corresponding node values are equal, `False` otherwise.

"Structurally identical" means: same shape (same nodes present in the same left/right positions) — not just same values in some order.

Example — these are identical:
```
     1                1
   // \\            // \\
  2     3           2    3
```

Example — these are **not** identical (different structure, even though same values overall):
```
    1                 1
   //                  \\
  2                      2
```

Example — these are **not** identical (same structure, different value):
```
     1                1
   // \\            // \\
  2     3           2    4
```

Try `is_same_tree(p, q)` — same return-and-combine recursive pattern you've used throughout. Think about: what should the base case be when *both* are `None`? What if only one is `None`? What do you combine when both exist?
"""

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return (p.data == q.data 
            and is_same_tree(p.left, q.left) 
            and is_same_tree(p.right, q.right))