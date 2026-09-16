"""
### Kth Smallest Element

Given an integer array `nums` and an integer `k`, return the **kth smallest element** in the array.

Note that it is the kth smallest element in **sorted order**, not the kth distinct element.

**Example:**

```text
Input:
nums = [7, 10, 4, 3, 20, 15]
k = 3

Output:
7
```

Because sorted order would be:

```text
[3, 4, 7, 10, 15, 20]
       ↑
   3rd smallest
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
def kth_smallest(nums, k):
    # your code
```
"""
import heapq

def kth_smallest(nums, k):
        heap = []

        for num in nums:
                heapq.heappush(heap, -num)

                if len(heap) > k:
                        heapq.heappop(heap)

        return -heap[0]

nums = [7, 10, 4, 3, 20, 15]
k = 3

print(f"kth_smallest({nums}, {k}): {kth_smallest(nums, k)}")