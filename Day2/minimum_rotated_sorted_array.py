from typing import List


class Solution():
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.l = 0
        self.r = len(nums) - 1
        self.result = nums[self.l]
        self.m = 0

    def min_rotated_array(self):
        while (self.l <= self.r):
            if (self.nums[self.r] > self.nums[self.l]):
                self.result = min(self.result, self.nums[self.l])
                break
            self.m = (self.l + self.r) // 2
            self.result = min(self.result, self.nums[self.m])

            if (self.nums[self.m] >= self.nums[self.l]):
                # we are in the left half, so let's search through the right half
                self.l = self.m + 1
            else:
                self.r = self.m - 1
        return self.result

    def binary_search(arr: List[int], target: int):

        left_index, right_index, mid_index = 0, len(arr) - 1, 0

        while (left_index <= right_index):

            mid_index = (left_index + right_index) // 2

            # if target is smaller than the mid index value, ignore the right half and focus on the left half
            if (arr[mid_index] > target):
                right_index = mid_index - 1

            # if target is greater than the mid index value, ignore the left half and focus on the right half
            elif (arr[mid_index] < target):
                left_index = mid_index + 1

            # means target is present at the mid index
            else:
                return mid_index

        # the element was not present
        return -1


nums = [4, 5, 6, 7, 8, 1, 2, 3]
instance_solution = Solution(nums=nums)
print(instance_solution.min_rotated_array())
