def ShopOLAP(N: int, items: list) -> list:

    items_dict = {}
    for i in range(N):
        key = items[i].split(' ')[0]
        value = int(items[i].split(' ')[1])
        if key in items_dict:
            items_dict[key] += value
        else:
            items_dict.update({key:value})

    items_list = []
    for key, value in items_dict.items():
        items_list.append(key + ' ' + str(value))
    items_list.sort()

    def get_end(item):
        return item[-1]

    items_list.sort(reverse=True, key=get_end)

    return items_list

