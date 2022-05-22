def squash_number_list(a: list) -> str:
    if a == []:
        return ""

    res = [[a[0], -1]]

    for i in range(1, len(a)):
        if a[i] - a[i - 1] == 1:
            res[-1][1] = a[i]
        else:
            res.append([a[i], -1])

    output = []

    for start, end in res:
        if end == -1 or end == start:
            output.append(f"{start}")
        else:
            output.append(f"{start}-{end}")

    return ",".join(output)
