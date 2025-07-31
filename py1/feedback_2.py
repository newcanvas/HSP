#1.
import os
def ReturnNameList(dir_path, file_extention, b_flag):
    files_list = []
    dirs_list = []
    final_list = []

    x = os.listdir(dir_path)
    for i in x:
        if i.split(sep='.')[-1] == file_extention:
            files_list.append(i)
        if i.split(sep='.')[-1] == i:
            dirs_list.append(i)
        orig_dirs_list = dirs_list
    if b_flag:
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
    assert final_list is not None
    return final_list

#2.
import os

import os
from PIL import Image

def scan_dir(path, ext):
    files = []
    for f in os.listdir(path):
        if ext == ".*" or f.endswith(ext):
            files.append(f)
    assert files is not None
    return files

def change_ext(old_ext, new_ext):
    r = scan_dir(".", old_ext)
    for i in r:
        im = Image.open(i)
        name = os.path.splitext(i)
        new_filename = f"{name[0]}_2.{new_ext}"
        im.save(new_filename)
        assert name != new_filename
