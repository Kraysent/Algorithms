def cocktail_cort(a: list) -> list:
    sorted = False
    left = 0
    right = len(a) - 1

    while left < right:
        for i in range(left, right):
            if a[i] > a[i + 1]:
                b = a[i]
                a[i] = a[i + 1]
                a[i + 1] = b

        right -= 1

        for i in range(left, right)[::-1]:
            if a[i] > a[i + 1]:
                b = a[i]
                a[i] = a[i + 1]
                a[i + 1] = b
        
        left += 1

    return a
