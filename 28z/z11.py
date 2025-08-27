def BigMinus(s1: str, s2: str) -> str:
    s1 = s1.replace("^", "**")
    s2 = s2.replace("^", "**")
    summ_list = [eval(s1), eval(s2)]
    return str(max(summ_list) - min(summ_list))

