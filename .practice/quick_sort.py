arr_nums = [2, 13, 9, 7, 0, 1, 56, 80, 8, 18, 15, 23, 11, 10, 5, 25, 19]


def swap_element(arr):
    first_element = arr[0]
    second_element = arr[1]
    if (first_element > second_element):
        arr[0] = second_element
        arr[1] = first_element
    return arr


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    elif (len(arr) == 2):
        new_arr = swap_element(arr)
        return new_arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort(arr_nums))
