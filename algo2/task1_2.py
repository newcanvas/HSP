'''
Задание 1.
Задача 1.
Метод, который перебирает всё дерево и прописывает каждому узлу его уровень.
Временная сложность: O(N), пространственная: O(N).
'''
def AddLevels(node) -> None:
    if node is None:
        return
    
    if node.Parent is None:
        node.Level = 0
    else:
        node.Level = node.Parent.Level + 1

    for child in node.Children:
        AddLevels(child)

    return

'''
Задание 1.
Задача 2.
Организация поддержки уровня узлов без анализа всего дерева.
Временная сложность: O(1), пространственная: O(1).
'''
class SimpleTreeNodeWithLevel:
	
    def __init__(self, val, parent, level):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
        self.Level = level # значение уровня, для корня будет 0, для остальных узлов - уровень родителя + 1.
