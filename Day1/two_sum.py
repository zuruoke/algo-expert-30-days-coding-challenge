from typing import List


class Solution:
    def __init__(self, num_list: List[int], target: int) -> None:
        self.num_list = num_list
        self.target = target
        self.num_dict = {}

    def getTwoSum(self):

        for i, num in enumerate(self.num_list):
            result: int = self.target - num
            if (result in self.num_dict):
                return [self.num_dict[result], i]
            self.num_dict[num] = i


num_list = [2, 1, 4, 11, 3, 5, 9, 0, 6]
target = 20

instance_solution = Solution(num_list=num_list, target=target)

print(instance_solution.getTwoSum())
