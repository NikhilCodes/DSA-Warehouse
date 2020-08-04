"""
ALGORITHM : Heap Sort
WORST CASE => {
    PERFORMANCE:  O(n log(n))
    SPACE:        O(1)
}
"""
from copy import deepcopy


def left_elem(index, n):
    node_index = index * 2 + 1
    if node_index >= n:
        node_index = index

    return node_index


def right_elem(index, n):
    node_index = index * 2 + 2
    if node_index >= n:
        node_index = index

    return node_index


def heapify(arr, i=None):  # Min Heap
    size = len(arr)
    if i is None:
        i = (len(arr) // 2) - 1

    left = left_elem(i, size)
    right = right_elem(i, size)

    min_child = left if arr[left] < arr[right] else right

    if arr[i] > arr[min_child]:
        arr[i], arr[min_child] = arr[min_child], arr[i]

    if i == 0:
        return arr

    return heapify(arr, i-1)


def heap_sort(arr):
    size = len(arr)

    for i in range(size-1):
        arr[i:] = heapify(arr[i:])

    return arr


if __name__ == "__main__":
    unsorted_arr = [6, 8, 1, 4, 2, 0]
    sorted_arr = heap_sort(unsorted_arr)
    print(sorted_arr)
    assert sorted_arr == sorted(unsorted_arr), "Invalid Heap Sort!"
