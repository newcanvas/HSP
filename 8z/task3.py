def EEC_help(arr1: list, arr2: list) -> bool:

    list1 = arr1
    list2 = arr2

    try:
        for i in range(len(list1)):
            list2.remove(list1[0])
            list1.remove(list1[0])
    except ValueError:
        return False

    return list1 == list2

