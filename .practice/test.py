from typing import List


def binary_search(arr: List[int], target: int):
    l = 0
    mid = 0
    r = len(arr) - 1

    while (l <= r):
        mid = (l + r) // 2
        if (r == target):
            return r
        if(l == target):
            return r
        if (target > arr[mid]):
            l = mid + 1
        elif (target < arr[mid]):
            r = mid - 1
        else:
            return mid
    return -1


arr = [1, 3, 5, 7, 8, 10, 16, 19, 21]
target = 16


def sort():
    return sorted("ananipyabbghcdecyuyyiypypypypypiptpyp")


# print(sort())

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = {}
    topKElements = []
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for _ in range(k):
        val = max(freq, key=freq.get)
        topKElements.append(val)
        del freq[val]

    return topKElements


nums = [1, 1, 1, 2, 2, 3, 6, 6, 8, 8, 9, 9, 9, 9]
k = 2


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = []
    postfix = []
    prefix_count = 1
    postfix_count = 1
    res = 1
    result = []
    for i in range(len(nums)):
        prefix_count *= nums[i]
        if i == 0:
            prefix.append(nums[i])
        else:
            prefix.append(prefix_count)

    for k in range(len(nums) - 1, -1, -1):
        postfix_count *= nums[k]
        if k == (len(nums) - 1):
            postfix.insert(0, nums[k])
        else:
            postfix.insert(0, postfix_count)

    for j in range(len(nums)):
        if j == 0:
            res = 1 * postfix[j + 1]
        elif j == (len(nums) - 1):
            res = prefix[j - 1] * 1
        else:
            res = prefix[j - 1] * postfix[j + 1]
        result.append(res)
    return result


print(productExceptSelf(nums=[1, 2, 3, 4]))
