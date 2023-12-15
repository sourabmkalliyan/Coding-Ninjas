def maxDepth(s:str) -> int:
    count = 0
    maxcount = 0
    n = len(s)
    for i in range(n):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
        maxcount = max(maxcount, count)
    return maxcount
    pass