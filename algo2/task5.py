def GenerateBBSTArray(a):
    a.sort()
    result = [None] * len(a)

    _fill_bbst_rec(a, result, 0, len(a) - 1, 0)

    return result


def _fill_bbst_rec(a, result, left, right, index):
    if left > right:
        return

    middle = (left + right) // 2
    result[index] = a[middle]

    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < len(a):
        _fill_bbst_rec(a, result, left, middle - 1, left_child)

    if right_child < len(a):
        _fill_bbst_rec(a, result, middle + 1, right, right_child)
