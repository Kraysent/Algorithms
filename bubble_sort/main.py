def bubble_sort(a: list) -> list:
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                is_sorted = False

                b = a[i]
                a[i] = a[i + 1]
                a[i + 1] = b

    return a