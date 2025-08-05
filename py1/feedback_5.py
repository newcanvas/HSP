import os
import re

def ReturnNameList(dir_path, file_extention, b_flag):
    files_list = []
    dirs_list = []
    final_list = []

    x = os.listdir(dir_path)
    for i in x:
        if '.' in i and re.fullmatch(file_extention, i.split('.')[-1]):
            files_list.append(i)
        elif '.' not in i:
            dirs_list.append(i)
        orig_dirs_list = dirs_list
    if b_flag == True:
        orig_dirs_list = dirs_list.copy()
        for dir in orig_dirs_list:
            new_dir_path = dir_path + '/' + dir
            x = os.listdir(new_dir_path)
            for i in x:
                if i.split(sep='.')[-1] == file_extention:
                    files_list.append(i)
                if i.split(sep='.')[-1] == i:
                    dirs_list.append(i)
    final_list.append(files_list)
    final_list.append(dirs_list)
    return final_list

def DeleteDir(path):
    search = ReturnNameList(path, ".*", False)
    if len(search[1]) > 0:
            return False
    for file in search[0]:
        os.remove(os.path.join(path,file))
    os.rmdir(path)
    return True
