def SumOfThe(N: int, data: list) -> int:
    for i in range(N):
        if data[i] == sum(data) - data[i]:
            return data[i]
        

