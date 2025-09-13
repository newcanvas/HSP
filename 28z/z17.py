import re

def LineAnalysis(line: str) -> bool:

    pattern = ''
    for i in range(len(line)):
        if i > 0 and line[i] == '*':
            pattern += line[i]
            break
        pattern += line[i]

    if pattern == '*':
        return len(re.findall(f'(?={re.escape(pattern)})', line)) == len(re.findall(re.escape('*'), line))
    return len(re.findall(f'(?={re.escape(pattern)})', line)) == len(re.findall(re.escape('*'), line)) - 1

