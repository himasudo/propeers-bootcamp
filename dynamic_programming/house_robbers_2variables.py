class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev1 = nums[0]
        prev2 = max(prev1, nums[1])

        for i in range(2, len(nums)):
            prev2, prev1 = max(prev1 + nums[i], prev2), prev2

        return prev2


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5, 1, 1, 5], 10),
        ([10], 10),
        ([0, 0, 0], 0),
        ([2, 1], 2),
        ([1, 3, 1, 3, 100], 103),
        ([10, 1, 1, 10, 1, 1, 10], 30),
    ]

    solution = Solution()

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.rob(nums.copy())
        status = "PASS" if result == expected else "FAIL"

        print(
            f"Test {i}: {status} | "
            f"Expected: {expected}, Got: {result}"
        )
