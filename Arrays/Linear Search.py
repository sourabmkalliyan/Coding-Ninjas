def linearSearch(n: int, num: int, arr: [int]) -> int:
    ans = -1
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return ans