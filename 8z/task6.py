def TRC_sort(arr: list) -> list:
    return TRC_sort_rec(arr, 0, [], [], [])

def TRC_sort_rec(arr, i, zeros, ones, twos):
    if i == len(arr):
        return zeros + ones + twos

    if arr[i] == 0:
        return TRC_sort_rec(arr, i+1, zeros+[0], ones, twos)
    if arr[i] == 1:
        return TRC_sort_rec(arr, i+1, zeros, ones+[1], twos)
    if arr[i] == 2:
        return TRC_sort_rec(arr, i+1, zeros, ones, twos+[2])

