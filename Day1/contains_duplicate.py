from typing import List


class Solution():
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.nums_dict = {}
        self.l, self.r = 0, 1

    def contains_duplicate(self) -> bool:
        for num in self.nums:
            if (num in self.nums_dict):
                return True
            self.nums_dict[num] = num
        return False

    def contains_duplicate_sliding_window_method(self) -> bool:
        self.nums.sort()
        while (self.r < len(self.nums)):
            if (self.nums[self.l] == self.nums[self.r]):
                return True
            self.r += 1
            self.l += 1
        return False


nums = [2, 11, 5, 6, 9, 3, 10, 50, 60, 90, 123]
instance_solution = Solution(nums=nums)
print(instance_solution.contains_duplicate())
print(instance_solution.contains_duplicate_sliding_window_method())
