def open_and_sum(inf_list: list) -> int:
    summ = 0
    for file in inf_list:
        try:
            current_file = open(file, 'rt')
            for line in current_file:
                summ+=int(line)
        except ValueError:
            return "Внутри файлов что-то кроме чисел"
        except Exception:
            return "Один из файлов поврежден, нужно разбираться"
        finally:
            current_file.close()
    return summ
