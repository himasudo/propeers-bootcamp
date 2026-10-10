class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i - 1])

        return dp[-1]


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
