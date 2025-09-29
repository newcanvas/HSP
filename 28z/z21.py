def BiggerGreater(input: str) -> str:

    new_string = list(input)
    i = len(new_string) - 1
    while i > 0 and new_string[i - 1] >= new_string[i]:
        i -= 1
    if i <= 0:
        return ''

    j = len(new_string) - 1
    while new_string[j] <= new_string[i - 1]:
        j -= 1
    new_string[i - 1], new_string[j] = new_string[j], new_string[i - 1]
    
    new_string[i : ] = new_string[len(new_string) - 1 : i - 1 : -1]

    return "".join(new_string)

