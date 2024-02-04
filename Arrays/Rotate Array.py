def rotateArray(arr: list, k: int) -> list:
    if k > len(arr):
        k = k % len(arr)

    last = arr[:k]
    arr[:-k] = arr[k:]
    arr[-k:] = last
    return arr