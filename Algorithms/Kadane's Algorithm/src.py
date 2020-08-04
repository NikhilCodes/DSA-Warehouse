"""
Using Kadane's Algorithm for solving maximum sub-array problem.

Example #1:
    Input  -> [-1, 2, 3, -2]
    Output -> [2, 3]

    As maximum possible sum of sub-array is 5.

Example #2:
    Input  -> [3, 5, -1, 8, -2, -4]
    Output -> [3, 5, -1, 8]

    As maximum possible sum of sub-array is 15.
"""
from copy import deepcopy


def get_max_sub_arr(arr):
    curr_max_sub_arr = []
    max_sum = 0
    res_sum = arr[0]
    res_arr = []

    for k in arr:
        if max_sum + k < k:
            max_sum = k
            curr_max_sub_arr = [k]
        else:
            max_sum += k
            curr_max_sub_arr.append(k)

        if res_sum < max_sum:
            res_sum = max_sum
            res_arr = deepcopy(curr_max_sub_arr)

    return res_sum, res_arr


if __name__ == '__main__':
    arr_ = [3, 5, -1, 8, -2, -4]
    max_sub_arr = get_max_sub_arr(arr_)
    print(max_sub_arr)
