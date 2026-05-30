# 1.
В каких случаях наиболее уместно обнуление переменных? Стоит ли это делать внутри функций каждый раз?
// Изначальный код:
```
def DeleteDir(path):
    search = ReturnNameList(path, ".*", False)
    if len(search[1]) > 0:
            return False
    for file in search[0]:
        os.remove(os.path.join(path,file))
    os.rmdir(path)
    return True
```
// Обнулила значения переменной с результатами поиска. Поправила названия переменной.
```
def DeleteDir(path):
    search_result = ReturnNameList(path, ".*", False)
    if len(search_result[1]) > 0:
            return False
    for file in search_result[0]:
        os.remove(os.path.join(path,file))
    os.rmdir(path)
    search_result = None
    return True
```
