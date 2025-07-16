#Рефлексия
#Зря использовала громоздкое решение с распаковкой и удалением, также можно было использовать уже существующую функцию посика.

#Решение
#3.1.
import os
from PIL import Image

def scan_dir(path, ext):
    files = []
    for f in os.listdir(path):
        if ext == ".*" or f.endswith(ext):
            files.append(f)
    return files
        
def change_ext(old_ext, new_ext):
    r = scan_dir(".", old_ext)
    for i in r:
        im = Image.open(i)
        name = os.path.splitext(i)
        new_filename = f"{name[0]}_2.{new_ext}"
        im.save(new_filename)

#3.2
import os
from PIL import Image, ImageDraw

def scan_dir(path, ext):
    files = []
    for f in os.listdir(path):
        if ext == ".*" or f.endswith(ext):
            files.append(f)
    return files
        
def change_ext(old_ext, new_ext):
    r = scan_dir(".", old_ext)
    for i in r:
        im = Image.open(i)
        draw = ImageDraw.Draw(im)
        width, height = im.size

        rect_w, rect_h = 100, 100
        rect_x0 = (width - rect_w) // 2
        rect_y0 = (height - rect_h) // 2
        rect_x1 = rect_x0 + rect_w
        rect_y1 = rect_y0 + rect_h
        draw.rectangle((rect_x0, rect_y0, rect_x1, rect_y1), outline="black")

        bbox = draw.multiline_textbbox((0, 0), "Hello,\nWorld!")
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        text_x = (width - text_w) // 2
        text_y = (height - text_h) // 2
        draw.multiline_text((text_x, text_y), "Hello,\nWorld!", fill="black", align="center")

        name = os.path.splitext(i)
        new_filename = f"{name[0]}_2.{new_ext}"
        im.save(new_filename)
        del draw
        im.show()

