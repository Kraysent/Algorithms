def gcd(num1: int, num2: int) -> int:
    """
    Given to integer numbers, find greates common divisor between them.

    General idea: reduce computation of GCD of `num1` and `num2` to computation of
    GCD of `num2` and `num1 - num2`.
    """

    if num1 == num2:
        return num1

    return gcd(num2, abs(num1 - num2))


if __name__ == "__main__":
    print(gcd(2342342, 2342342))
