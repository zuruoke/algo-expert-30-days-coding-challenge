from typing import List


class Solution():
    def longest_increasing_subsequence(self, nums: List[int]):
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if (nums[i] < nums[j]):
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)


nums = [10, 9, 2, 5, 3, 7, 101, 18, 45, 68, 13, 56, 0, 21, 18]
instance_solution = Solution()

print(instance_solution.longest_increasing_subsequence(nums))
