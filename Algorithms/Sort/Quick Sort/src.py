"""
ALGORITHM : Quick Sort
WORST CASE => {
    PERFORMANCE:  O(n^2))
    SPACE:        O(log(n))
}
AVERAGE CASE => {
    PERFORMANCE:  O(n log(n))
}
"""


def quick_sort(arr):
    pivot = 0
    size = len(arr)

    if size == 1 or size == 0:
        return arr

    for i in range(1, size):
        if arr[i] < arr[pivot]:
            if i == pivot + 1:
                arr[i], arr[pivot] = arr[pivot], arr[i]
            else:
                arr[pivot], arr[i], arr[pivot + 1] = arr[i], arr[pivot + 1], arr[pivot]
            pivot += 1

    arr[:pivot + 1] = quick_sort(arr[:pivot + 1])
    arr[pivot + 1:] = quick_sort(arr[pivot + 1:])

    return arr


if __name__ == "__main__":
    unsorted_arr = [6, 9, 5, 2, 7, 3, 1]
    sorted_arr = quick_sort(unsorted_arr)
    print(sorted_arr)
