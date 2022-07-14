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


def binary_search(arr, target):
    l = 0
    r = len(arr) - 1
    mid = 0

    while l <= r:
        mid = (r + l + 1) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return False


def searchMatrix(matrix, target: int) -> bool:
    l = 0
    r = len(matrix) - 1

    while l <= r:
        mid = (r + l + 1) // 2

        if target == max(matrix[mid]) or target == min(matrix[mid]):
            return True
        elif target < max(matrix[mid]):
            if target > min(matrix[mid]):
                r = mid
                matrix[r].pop(-1), matrix[r].pop(0)
                return binary_search(matrix[r], target)
            else:
                r = mid - 1
                if binary_search(matrix[r], target):
                    return True

        else:
            l = mid + 1

    return False


print(searchMatrix(two_2d_arr, 109))
#print(binary_search([1, 2, 3, 5, 6, 9, 10, 12], 10))
