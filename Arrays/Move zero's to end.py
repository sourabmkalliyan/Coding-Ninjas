def moveZeros(n: int,  a: [int]) -> [int]:
    l = 0
    for r in range(len(a)):
        if a[r]:
            a[l], a[r] = a[r], a[l]
            l += 1
    return a