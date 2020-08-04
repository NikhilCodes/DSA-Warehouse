def find_substring(string: str, substring: str) -> int:
    l1 = len(string)
    l2 = len(substring)

    for i in range(l1 - l2 + 1):
        status = True
        for j in range(l2):
            if string[i+j] != substring[j]:
                status = False

        if status:
            return i


if __name__ == '__main__':
    s = "doo-foo-boo"
    ss = "boo"

    pos = find_substring(s, ss)
    print("Substring found at position {}.".format(pos))
