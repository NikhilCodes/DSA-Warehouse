"""
ALGORITHM : Merge Sort
WORST CASE => {
    PERFORMANCE:  O(n log(n))
    SPACE:        O(n)
}
"""


def merge_sort(arr):
    size = len(arr)

    if size == 1:
        return arr
    elif size == 2:
        if arr[1] > arr[0]:
            return [arr[0], arr[1]]

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            merged_arr.append(right.pop(0))
        else:
            merged_arr.append(left.pop(0))
    merged_arr += left + right
    return merged_arr


if __name__ == '__main__':
    sorted_arr = merge_sort([8, 4, 2, 9, 1, 3])
    print(sorted_arr)
