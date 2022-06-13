from typing import List


class Solution:
    def longest_consecutive_sequence(self, nums: List[int]):
        numSet = set(nums)
        longest_consec_seq = 0

        for n in nums:
            length = 0

            if (n - 1) not in numSet:
                while (n + length) in numSet:
                    length += 1
            longest_consec_seq = max(length, longest_consec_seq)
        return longest_consec_seq

    def naive_soln(self, nums: List[int]):
        nums.sort()
        longest = 1

        for i in range(len(nums) - 1):
            j = i
            length = 1
            while(j < len(nums) - 1 and nums[j + 1] == nums[j] + 1):
                length += 1
                j += 1
            longest = max(length, longest)
        return longest


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
instance_solution = Solution()
print(instance_solution.longest_consecutive_sequence(nums=nums))
print(instance_solution.naive_soln(nums))
