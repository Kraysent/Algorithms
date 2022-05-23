def get_fibonacci_number(index: int) -> int:
    a = 0
    b = 1
    i = 2

    if index == 0:
        return a
    elif index == 1:
        return b

    while i < index:
        c = a + b
        a = b
        b = c
        i += 1

    return b