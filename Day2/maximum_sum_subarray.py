from typing import List


class Solution():

    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        self.result: List[int] = []
        self.maxSub = nums[0]
        self.curSum = 0

    def naive_max_sub_array(self):
        for i in range(0, len(self.nums)):
            temp_list: List[int] = []
            for j in range(i, len(self.nums)):
                temp_list.append(self.nums[j])
                self.result.append(sum(temp_list))
        return max(self.result)

    def best_case_soln_max_sub_array(self):

        for n in self.nums:
            if self.curSum < 0:
                self.curSum = 0

            self.curSum += n
            self.maxSub = max(self.maxSub, self.curSum)
        return self.maxSub


nums = [-2, 1, -3]
instance_solution_1 = Solution(nums=nums)
instance_solution_2 = Solution(nums=nums)
print(instance_solution_1.naive_max_sub_array())
print(instance_solution_2.best_case_soln_max_sub_array())
