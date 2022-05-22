def binary_search(a: list, value: int) -> int:
    left = 0
    right = len(a)

    while left < right:
        i = left + (right - left) // 2

        if a[i] == value:
            return i
        elif a[i] > value:
            right = i
        else:
            left = i + 1

    return -1