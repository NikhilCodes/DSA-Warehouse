"""
ALGORITHM : Selection Sort
WORST CASE => {
    PERFORMANCE:  O(n^2)
    SPACE:        O(1)
}
"""


def selection_sort(arr):
    size = len(arr)

    for i in range(size):
        min_val_index = i
        for j in range(i, size):
            if arr[min_val_index] > arr[j]:
                min_val_index = j

        arr[min_val_index], arr[i] = arr[i], arr[min_val_index]

    return arr


if __name__ == '__main__':
    array = [8, 7, 6, 5, 4, 3, 2, 1]
    sorted_arr = selection_sort(array)

    print(sorted_arr)
