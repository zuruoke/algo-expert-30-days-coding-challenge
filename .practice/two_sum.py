from typing import List
from unittest import result


def naive_soln(arr: List[int], target: int):
    for i in range(len(arr)):
        for k in range(i + 1, len(arr), 1):
            result: int = arr[i] + arr[k]
            if (result == target):
                return [i, k]


def best_soln(arr: List[int], target: int):
    memo: dict = {}
    for j in range(len(arr)):
        result: int = target - arr[j]
        if (result in memo):
            return [memo[result], j]
        memo[arr[j]] = j
    return - 1


def window_slider_mthd(arr: List[int], target: int):
    l, r = 0, len(arr) - 1
    arr.sort()
    while (l <= r):
        result = arr[r] + arr[l]
        if (result < target):
            l += 1
        elif (result > target):
            r -= 1
        else:
            return [l, r]


arr = [1, 3, 4, 11, 2, 8, 10, 7, 9, 12, 21]
target = 33


#print(window_slider_mthd(arr=arr, target=target))


two_2d_arr = [

    [], [1], [1, 2], [1, 3]
]
