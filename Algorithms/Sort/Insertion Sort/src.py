"""
ALGORITHM : Insertion Sort
WORST CASE => {
    PERFORMANCE:  O(n^2)
    SPACE:        O(1)
}
"""


def insertion_sort(arr):
    for k in range(1, len(arr)):
        for i in range(k, 0, -1):
            # This Block runs `n(n+1)/2` times hence T(N^2)
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = [arr[i - 1], arr[i]]

    return arr


if __name__ == '__main__':
    array = [8, 7, 6, 5, 4, 3, 2, 1]
    sorted_arr = insertion_sort(array)
    print(sorted_arr)
