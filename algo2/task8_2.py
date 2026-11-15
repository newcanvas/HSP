'''
Задание 8.
Задача 2.
Направленный граф, представленный матрицей смежности.
Временная сложность добавления/удаления ребра O(1), пространственная O(1).
'''
from task8 import SimpleGraph


class DirectedGraph(SimpleGraph):

    def IsEdge(self, v1, v2):
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0

    def IsCyclic(self): 
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE] * self.max_vertex

        def visit(v):
            color[v] = GRAY

            for neighbour in range(self.max_vertex):
                if self.m_adjacency[v][neighbour] != 1:
                    continue

                if color[neighbour] == GRAY:
                    return True

                if color[neighbour] == WHITE and visit(neighbour):
                    return True

            color[v] = BLACK
            return False

        for v in range(self.max_vertex):
            if self.vertex[v] is not None and color[v] == WHITE:
                if visit(v):
                    return True

        return False

'''
Рефлексия.
2. Отдельную проверку распределения значений я не делала: в моём решении дерево
строится из отсортированного массива, а корнем каждого поддерева
всегда выбирается медиана, поэтому свойство упорядоченности (все значения в левом
поддереве меньше узла, в правом больше) выполняется самим построением. Рекомендованный
способ надежнее, если дерево могли изменить вручную.

3. Проверку сбалансированности я реализовала двумя способами, и оба совпадают с
рекомендованным по идее. Разница в реализации:
в IsBalanced высота считается за один проход с ранним выходом через -1, а в
IsBalanced2 высота пересчитывается для каждого узла заново.
'''
