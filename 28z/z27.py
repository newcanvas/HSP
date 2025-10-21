def Football(F: list, N: int) -> bool:
    F1 = F.copy()

    affected_range = set()

    for i in range(N-1, 0, -1):
        if F1[i] < F1[i - 1]:
            j = i - 1
            while j >= 0 and F1[i] < F1[j]:
                j -= 1

            swap_pos = j + 1
            F1[i], F1[swap_pos] = F1[swap_pos], F1[i]

            affected_range.add(i)
            affected_range.add(swap_pos)

            if len(affected_range) > 2:
                min_pos = min(affected_range)
                max_pos = max(affected_range)

                for pos in range(min_pos, max_pos + 1):
                    if pos not in affected_range:
                        return False

    return F != F1

