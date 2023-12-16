# Isomorphic Strings Coding Ninjas

def areIsomorphic(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return 0
    mapOT, mapTO = {}, {}
    for i in range(len(str1)):
        c1, c2 = str1[i], str2[i]
        if ((c1 in mapOT and mapOT[c1] != c2 or c2 in mapTO and mapTO[c2] != c1)):
            return 0
        mapOT[c1] = c2
        mapTO[c2] = c1
    return 1
    pass