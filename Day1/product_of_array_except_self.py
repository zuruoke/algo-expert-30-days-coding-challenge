from functools import reduce, total_ordering
from sys import prefix
from typing import List
from operator import mul


class Solution():
    def __init__(self, nums) -> None:
        self.nums = nums
        self.result: List[int] = []
        self.prefix = []
        self.prefix.append(nums[0])
        self.postfix = []
        self.postfix.append(nums[-1])

    def naive_solution(self) -> List[int]:
        for num in self.nums:
            temp = self.nums.copy()
            temp.remove(num)
            total = reduce(mul, temp, 1)
            self.result.append(total)
        return self.result

    def naive_pre_pos_fix(self) -> List[int]:
        for i, num in enumerate(self.nums):
            if (i == 0):
                continue
            total = self.prefix[-1] * num
            self.prefix.append(total)
        for i in range(len(self.nums) - 1, -1, -1):
            if (i == len(self.nums) - 1):
                continue
            total = self.postfix[-1] * nums[i]
            self.postfix.append(total)
        self.postfix.reverse()

        for i, num in enumerate(self.nums):
            if (i == 0):
                total = self.postfix[i + 1]
                self.result.append(total)
            elif (i == len(self.nums) - 1):
                total = self.prefix[i - 1]
                self.result.append(total)
            else:
                total = self.prefix[i - 1] * self.postfix[i + 1]
                self.result.append(total)
        return self.result


nums = [1, 2, 3, 4]
instance_solution_1 = Solution(nums=nums)
instance_solution_2 = Solution(nums=nums)
print(instance_solution_1.naive_pre_pos_fix())
print(instance_solution_2.naive_solution())


# def fin():
#     res = [1] * (len(nums))

#     prefix = 1
#     for i in range(len(nums)):
#         res[i] = prefix
#         prefix *= nums[i]
#     print("prefix is {}".format(res))
#     postfix = 1
#     for i in range(len(nums) - 1, -1, -1):
#         res[i] *= postfix
#         postfix *= nums[i]
#     print("postfix is {}".format(res))
#     return res


# print(fin())
