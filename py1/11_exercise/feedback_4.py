def final(inf_list: list) -> list:
    summ = 0
    for file in inf_list:
        current_file = file_sum(file)
        if current_file[1] == 0:
            summ += current_file[0]
        else:
            return [0, current_file[1]]
    return [summ, 0]

def file_sum(file):
    try:
        with open(file, 'rt') as files:
            summ = 0
            for i in range(3):
                line = files.readline()
                summ += int(line)
            return [summ, 0]
    except FileNotFoundError:
        return [0, 2]
    except Exception as ex:
        return [0, 1]
