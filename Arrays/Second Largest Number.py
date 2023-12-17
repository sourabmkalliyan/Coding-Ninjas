# Brute Force Approach

def getSecondOrderElements(n: int, a: [int]) -> [int]:
    ans = []
    if n == 1 or n == 0:
        ans.append(-1)
        ans.append(-1)
        return ans
    else:
        a.sort()
        large = a[n - 2]
        small = a[1]
        ans.append(large)
        ans.append(small)
        return ans

# Better Methode

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    ans = []
    small = float('inf')
    s_small = float('inf')
    large = float('-inf')
    s_large = float('-inf')
    for i in range(n):
        small = min(small, a[i])
        large = max(large, a[i])
    for i in range(n):
        if a[i] < s_small and a[i] != small:
            s_small = a[i]
        elif a[i] > s_large and a[i] != large:
            s_large = a[i]
    ans.append(s_large)
    ans.append(s_small)
    return ans

#Optimal Approach

def secondLargest(n, a):
    large = float('-inf')
    s_large = float('-inf')
    for i in range(n):
        if a[i] > large:
            s_large = large
            large = a[i]
        elif a[i] > s_large and a[i] != large:
            s_large = a[i]
    return s_large


def secondSmallest(n, a):
    small = float('inf')
    s_small = float('inf')
    for i in range(n):
        if a[i] < small:
            s_small = small
            small = a[i]
        elif a[i] < s_small and a[i] != small:
            s_small = a[i]
    return s_small



def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    ans = []
    s_large = secondLargest(n, a)
    s_small = secondSmallest(n, a)
    ans.append(s_large)
    ans.append(s_small)
    return ans
