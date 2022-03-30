from typing import List


class Solution():
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.result: List[List[int]] = []

    def three_sum_equal_zero(self):
        if (len(self.nums) < 3):
            return []
        self.nums.sort()

        for i, n in enumerate(self.nums):
            if (i > 0 and n == self.nums[i - 1]):
                continue
            l, r = i + 1, len(self.nums) - 1

            while l < r:
                target = 0 - n
                sum_result = self.nums[l] + self.nums[r]
                if (target == sum_result):
                    self.result.append([n, self.nums[l], self.nums[r]])
                    l = l + 1
                    while (self.nums[l - 1] == self.nums[l] and l < r):
                        l = l + 1
                elif (sum_result < target):
                    l = l + 1

                else:
                    r = r - 1

        return self.result


nums = [-2, -2, 0, 0, 2, 2]
instance_solution = Solution(nums=nums)
print(instance_solution.three_sum_equal_zero())
