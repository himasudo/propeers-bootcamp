class Solution:
    def rob(self, nums: list[int]) -> int:  
        def recursive_rob(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + recursive_rob(i + 2), recursive_rob(i+1))

        return recursive_rob(0)


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
