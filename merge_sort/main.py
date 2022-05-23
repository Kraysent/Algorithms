def merge_arrays(a: list, b: list) -> list:
    i1 = 0
    i2 = 0
    res = []

    while i1 < len(a) and i2 < len(b):
        if a[i1] < b[i2]:
            res.append(a[i1])
            i1 += 1
        else:
            res.append(b[i2])
            i2 += 1

    while i1 < len(a):
        res.append(a[i1])
        i1 += 1

    while i2 < len(b):
        res.append(b[i2])
        i2 += 1

    return res


def merge_sort(a: list) -> list:
    if len(a) < 2:
        return a
    elif len(a) == 2:
        return [min(a), max(a)]
    else:
        return merge_arrays(merge_sort(a[: len(a) // 2]), merge_sort(a[len(a) // 2 :]))
