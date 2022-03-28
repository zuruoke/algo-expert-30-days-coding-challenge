from typing import List


class Solution():
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.result = max(nums)
        self.curMin = 1
        self.curMax = 1

    def get_product_subarray(self):
        for num in self.nums:
            if (num == 0):
                self.curMax = 1
                self.curMin = 1
                continue
            tmp = self.curMax * num
            self.curMax = max(num * self.curMax, num * self.curMin, num)
            self.curMin = min(tmp, num * self.curMin, num)
            self.result = max(self.result, self.curMax)
        return self.result


nums = [2, 4 - 5, -4, -10]
instance_solution = Solution(nums=nums)
print(instance_solution.get_product_subarray())
