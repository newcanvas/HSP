def final(inf_list: list) -> dict:
    summ = 0
    for file in inf_list:
        current_file = file_sum(file)
        if current_file['error_code'] == 0:
            summ += current_file['summ']
        else:
            return {'summ': 0, 'error_code': current_file['error_code']}
    return {'summ': summ, 'error_code': 0}

def file_sum(file):
    try:
        with open(file, 'rt') as files:
            summ = 0
            for i in range(3):
                line = files.readline()
                summ += int(line)
            return {'summ': summ, 'error_code': 0}
    except FileNotFoundError:
        return {'summ': 0, 'error_code': 2}
    except Exception as ex:
        return {'summ': 0, 'error_code': 1}
