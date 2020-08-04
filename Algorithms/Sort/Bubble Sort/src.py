"""
ALGORITHM : Bubble Sort
WORST CASE => {
    PERFORMANCE:  O(n^2)
    SPACE:        O(1)
}
"""


def bubble_sort(arr):
    size = len(arr)

    if size < 2:
        return arr

    for i in range(size-1, 0, -1):
        for j in range(len(arr[:i])):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    array = [3, 7, 6, 5, 4, 8, 2, 1]
    sorted_arr = bubble_sort(array)

    print(sorted_arr)
