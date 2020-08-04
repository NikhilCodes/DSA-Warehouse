"""
ALGORITHM : Binary Search
WORST CASE => {
    PERFORMANCE:  O(n)
    SPACE:        O(1)
}
"""


def linear_search(arr, key):
    size = len(arr)
    for i in range(size):
        if arr[i] == key:
            return True, i

    return False, None


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    found, index = linear_search(a, 4)

    if found:
        print("Found at position {}".format(index))
    else:
        print("Not Found!")
