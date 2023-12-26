def binarySearch(nums: [int], low: int, high: int, target: int):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return binarySearch(nums, mid + 1, high, target)
    elif target < nums[mid]:
        return binarySearch(nums, low, mid - 1, target)


def search(nums: [int], target: int):
    n = len(nums)
    return binarySearch(nums, 0, n - 1, target)


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
target = int(input())
print(search(arr, target))