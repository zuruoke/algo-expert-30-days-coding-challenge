from turtle import width
from typing import List


class Solution():

    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.result: int = 0

    def naive_solution(self):
        for l in range(len(self.nums)):
            for r in range(l + 1, len(self.nums), 1):
                # get the area
                width = r - l
                height = min(self.nums[l], self.nums[r])
                area = width * height
                self.result = max(area, self.result)
        return self.result

    def best_solution_for_container_with_most_water(self):
        l, r = 0, len(self.nums) - 1

        while l <= r:
            width = r - l
            height = min(self.nums[l], self.nums[r])
            area = width * height
            self.result = max(area, self.result)
            if (self.nums[r] > self.nums[l]):
                l = l + 1
            else:
                r = r - 1
        return self.result


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
instance_solution = Solution(nums=heights)
print(instance_solution.best_solution_for_container_with_most_water())
