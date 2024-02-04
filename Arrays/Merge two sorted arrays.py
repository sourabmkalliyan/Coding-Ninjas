def sortedArray(a: [int], b: [int]) -> [int]:
    a = set(a)
    b = set(b)
    return sorted(a.union(b))