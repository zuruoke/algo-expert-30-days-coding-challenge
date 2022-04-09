
def getSum(a: int, b: int) -> int:
    mask = -1

    while (b & mask) > 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return (a & mask) if b > 0 else a


print(getSum(a=5, b=9))
