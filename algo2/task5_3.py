'''
Задание 5.
Задача 2.
Оцените, насколько поиск узла в дереве, представленном в виде массива, эффективнее (или неэффективнее) поиска узла в классическом дереве с указателями.

Сложность будет одинаковой. Для сбалансированного дерева O(log N), для несбалансированного O(N).
'''

'''
Задание 5.
Задача 3.
Метод удаления узла из двоичного дерева, заданного в виде массива.
Временная сложность: O(N log N), пространственная: O(N).
'''


def DeleteNode(a, key):
    values = a.copy()

    if key not in values:
        return a

    values.remove(key)
    values.sort()

    result = [None] * len(values)

    _fill_bbst(values, result, 0, len(values) - 1, 0)

    return result


def _fill_bbst(a, result, left, right, index):
    if left > right or index >= len(result):
        return

    middle = left + _complete_left_size(right - left + 1)
    result[index] = a[middle]

    _fill_bbst(a, result, left, middle - 1, 2 * index + 1)

    _fill_bbst(a, result, middle + 1, right, 2 * index + 2)


def _complete_left_size(n):
    if n <= 1:
        return 0

    last_level_capacity = 1
    while last_level_capacity * 2 <= n:
        last_level_capacity *= 2

    last_level_nodes = n - last_level_capacity + 1
    left_last = min(last_level_capacity // 2, last_level_nodes)
    left_full = last_level_capacity // 2 - 1

    return left_full + left_last

'''
Задание 5.
Задача 4.
Ответьте на вопрос с картинки.

Насколько я понимаю, это невозможно. Только в том случае, если дерево уже отсортировано.
'''


'''
Рефлексия.
3. Общий алгоритм соответствует эталонному.

4. Мой алгоритм менее удачный, сделала его по аналогии с WideAllNodes. А можно было вынести обработку во внещнюю логику.

5. В целом алгоритм аналогичный, но не учла моменты про один преффикс и и одинаковые ключи.

'''
