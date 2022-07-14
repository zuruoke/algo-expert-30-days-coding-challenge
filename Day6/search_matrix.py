from typing import List


class Solution():
    def __init__(self, target: int) -> None:
        self.target = target

    def __binary_search(self, arr: List[int]) -> bool:
        l = 0
        r = len(arr) - 1
        mid = 0

        while l <= r:
            mid = (r + l + 1) // 2
            if arr[mid] == self.target:
                return True
            elif self.target < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

    def search_matrix(self, matrix: List[List[int]]) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (r + l + 1) // 2

            if self.target == max(matrix[mid]) or self.target == min(matrix[mid]):
                return True
            elif self.target < max(matrix[mid]):
                if self.target > min(matrix[mid]):
                    r = mid
                    matrix[r].pop(-1), matrix[r].pop(0)
                    return self.__binary_search(matrix[r])
                else:
                    r = mid - 1
                    if self.__binary_search(matrix[r]):
                        return True

            else:
                l = mid + 1

        return False


two_2d_arr = [
    [1, 3, 4, 7],
    [9, 11, 12, 16],
    [19, 20, 21, 22],
    [23, 29, 32, 33],
    [36, 37, 39, 40],
    [43, 49, 52, 63],
    [79, 80, 90, 92],
    [94, 97, 100, 101],
    [102, 108, 109, 112],
    [113, 119, 120, 121]
]

instance_solution = Solution(119)

print(instance_solution.search_matrix(two_2d_arr))
