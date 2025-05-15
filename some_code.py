def FindNum(list1: list, n: int):
    ind = -1
    for i in range(len(list1)):
        if list1[i] == n:
            ind = i
    return ind
    
print(FindNum([1,2,3,5], 5))
