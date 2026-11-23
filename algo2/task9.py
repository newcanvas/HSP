from task1 import SimpleTree


def CollectEvenSubtrees(node, result) -> int:
    size = 1

    for child in node.Children:
        size += CollectEvenSubtrees(child, result)

    if size % 2 == 0 and node.Parent is not None:
        result.append(node.Parent)
        result.append(node)

    return size


def EvenTrees(self) -> list:
    result = []

    if self.Root is None:
        return result

    CollectEvenSubtrees(self.Root, result)

    return result

SimpleTree.EvenTrees = EvenTrees
