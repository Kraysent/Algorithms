def to_binary_form(number: int) -> list:
    if number == 0: return [0]

    res = []

    while number != 0:
        res.append(number % 2)
        number = number // 2

    res.reverse()

    return res
