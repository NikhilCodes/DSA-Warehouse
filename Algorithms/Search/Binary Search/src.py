"""
ALGORITHM : Binary Search
WORST CASE => {
    PERFORMANCE:  O(log n)
    SPACE:        O(1)
}
"""


def binary_search(arr, key, _mid=None):
    if _mid is None:
        _mid = len(arr) // 2

    if arr[_mid] == key:
        return True, _mid

    if _mid == 0:
        return False, None

    step = min(_mid, len(arr) - _mid) + 1

    if key < arr[_mid]:
        _mid -= step // 2
    else:
        _mid += step // 2

    return binary_search(arr, key, _mid)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    found, index = binary_search(a, 9)

    if found:
        print("Found at position {}".format(index))
    else:
        print("Not Found!")
