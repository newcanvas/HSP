def WordSearch(len: int, s: str, subs: str) -> list:
    import textwrap, re
    splits = textwrap.wrap(s, width=len)

    final_list = []
    for i in splits:
        final_list.append(int(bool(re.search(rf'\b{subs}\b', i))))

    return final_list


