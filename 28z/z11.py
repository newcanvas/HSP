def BigMinus(s1: str, s2: str) -> str:
    
    if len(s1) > len(s2) or (len(s1) == len(s2) and s1 >= s2):
        max_s, min_s = s1, s2
    else:
        max_s, min_s = s2, s1

    max_s, min_s = list(max_s[::-1]), list(min_s[::-1])
    result = []
    surplus = 0

    for i in range(len(max_s)):
        d1 = int(max_s[i])
        if i < len(min_s):
            d2 = int(min_s[i])
        else:
            d2 = 0

        d = d1 - d2 - surplus
        if d < 0:
            d += 10
            surplus = 1
        else:
            surplus = 0

        result.append(str(d))

    while len(result) > 1 and result[-1] == "0":
        result.pop()

    return "".join(result[::-1])


