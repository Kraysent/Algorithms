def biggest_sum_subarray(a: list) -> int:
    s = 0
    biggest_sum = 0

    for x in a:
        s = max(0, s + x)
        biggest_sum = max(biggest_sum, s)

    return biggest_sum
