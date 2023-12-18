# Remove Duplicates - Coding Ninjas 
def removeDuplicates(arr,n):
    new = []
    new.append(arr[0])
    for i in range(1,n):
        if arr[i-1] != arr[i]:
            new.append(arr[i])
    return len(new)