def MaximumDiscount(N: int, price: list) -> int:

    price.sort(reverse=True)
    bulk = []
    summ = 0
    for i in range(N):
        bulk.append(price[i])
        if len(bulk) % 3 == 0:
            summ += min(bulk)
            bulk = []

    return summ

