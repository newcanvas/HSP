def digital_rain(col: str) -> str:

    col_map = {0: len(col)}
    current_sum = 0
    max_len = 0
    final_index = len(col)

    for i in range(len(col)-1, -1, -1):
        if col[i] == '1':
            current_sum += 1
        else:
            current_sum -= 1

        if current_sum in col_map:
            new_len = col_map[current_sum] - i
            if new_len > max_len:
                max_len = new_len
                final_index = col_map[current_sum]
        else:
            col_map[current_sum] = i

    if max_len == 0:
        return ''

    return col[final_index - max_len:final_index]

