def S(A: list, N: int) -> list:

    B = []
    for i in range(N):
        for j in range(N-i):
            k = i+j
            B.append(max(A[j:k+1]))

    return B

def TransformTransform(A: list, N: int) -> bool:

    summ = sum(S(S(A, N), len(S(A, N))))

    return summ // 2 == 0

