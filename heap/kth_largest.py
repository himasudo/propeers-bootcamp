"""
### Kth Largest Element

Given an integer array `nums` and an integer `k`, return the **kth largest element** in the array.

Note that it is the kth largest element in **sorted order**, not the kth distinct element.

**Example:**

```text
Input:
nums = [5, 11, 3, 9, 15, 2, 8]
k = 3

Output:
9
```

**Constraints:**

```text
1 <= k <= len(nums)
1 <= len(nums) <= 100000
-10000 <= nums[i] <= 10000
```

**Requirement:** Solve it using a heap. Avoid sorting the entire array.

Implement:

```python
def kth_largest(nums, k):
    # your code
```
"""
import heapq

def kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

# test
nums = [10, 4, 12, 3, 20, 7]
k = 2

print(f"kth_largest({nums}, {k}): {kth_largest(nums, k)}")