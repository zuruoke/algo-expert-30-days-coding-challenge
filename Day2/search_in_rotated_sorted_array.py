from typing import List


class Solution():
    def __init__(self, nums: List[int], target: int) -> None:
        self.nums = nums
        self.target = target
        self.l = 0
        self.r = len(nums) - 1

    def search_in_rotated_array(self):

        while (self.l <= self.r):
            mid = (self.l + self.r) // 2
            if (self.target == self.nums[mid]):
                return mid

            # left sorted portion
            if (self.nums[self.l] <= self.nums[mid]):
                if (self.target > self.nums[mid] or self.target < self.nums[self.l]):
                    self.l = mid + 1
                else:
                    self.r = mid - 1

            # right sorted portion

            else:
                if (self.target < self.nums[mid] or self.target > self.nums[self.r]):
                    self.r = mid - 1
                else:
                    self.l = mid + 1
        return - 1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

instance_solution = Solution(nums=nums, target=target)
print(instance_solution.search_in_rotated_array())
