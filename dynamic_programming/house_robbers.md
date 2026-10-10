# ProPeers Bootcamp Homework — House Robber

Medium

Dynamic Programming · Arrays · Recursion

[LeetCode Problem 198 — House Robber](https://leetcode.com/problems/house-robber/)

## Problem Statement

You are a professional robber planning to rob houses along a street.

Each house contains a certain amount of money, represented by an integer array `nums`, where `nums[i]` represents the amount of money in the `i-th` house.

However, there is one restriction:

You cannot rob two adjacent houses. If you rob two neighboring houses, their security systems will automatically trigger an alarm.

Given the integer array `nums`, return the maximum amount of money you can rob without triggering the alarm.

## Examples

### Example 1

Input:

```
nums = [1, 2, 3, 1]
```

Output:

```
4
```

Explanation:

Rob house 0 (₹1) and house 2 (₹3).

Maximum amount = 1 + 3 = 4.

### Example 2

Input:

```
nums = [2, 7, 9, 3, 1]
```

Output:

```
12
```

### Example 3

Input:

```
nums = [5, 1, 1, 5]
```

Output:

```
10
```

## Constraints

- `1 <= len(nums) <= 100`
- `0 <= nums[i] <= 400`
- You can rob any number of houses, including skipping houses.
- You must maximize the total amount robbed.
- You cannot rob two consecutive houses.

## Python Starter Code

Your task is to solve the problem using four different approaches.

### Approach 1 — Recursion

Implement a pure recursive solution without using memoization.

```
class Solution:    def rob(self, nums: list[int]) -> int:        # Write your recursive solution here        pass
```

### Approach 2 — Memoization (Top-Down DP)

Optimize the recursive solution using a Python list to store previously computed results.

```
class Solution:    def rob(self, nums: list[int]) -> int:        n = len(nums)        dp = [-1] * n        # Write your memoized solution here        pass
```

### Approach 3 — Tabulation (Bottom-Up DP)

Solve the problem iteratively by building a DP table.

```
class Solution:    def rob(self, nums: list[int]) -> int:        n = len(nums)        dp = [0] * n        # Write your tabulation solution here        pass
```

### Approach 4 — Space-Optimized DP

Optimize your tabulation solution so that it uses only two variables instead of an entire DP array.

```
class Solution:    def rob(self, nums: list[int]) -> int:        # Write your space-optimized solution here        pass
```

## Additional Test Cases

Use these to verify your implementations.

Test 1

[1,2,3,1]

Expected output

4

Test 2

[2,7,9,3,1]

Expected output

12

Test 3

[5,1,1,5]

Expected output

10

Test 4

[10]

Expected output

10

Test 5

[0,0,0]

Expected output

0

Test 6

[2,1]

Expected output

2

Test 7

[1,3,1,3,100]

Expected output

103

Test 8

[10,1,1,10,1,1,10]

Expected output

30

## Homework Requirements

For each of the four approaches, determine:

1. Time complexity — Big-O notation.
2. Auxiliary space complexity — including recursion stack space.
3. Base cases — which cases terminate your recursion or initialize your DP.
4. Correctness — verify your solution against the provided test cases.

Important: Solve the approaches in order: Recursion → Memoization → Tabulation → Space Optimization.
