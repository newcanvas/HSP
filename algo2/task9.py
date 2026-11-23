from task1 import SimpleTree

def EvenTrees(self) -> list:
    result = []

    if self.Root is None:
        return result

    def collect(node) -> int:
        size = 1

        for child in node.Children:
            size += collect(child)

        if size % 2 == 0 and node.Parent is not None:
            result.append(node.Parent)
            result.append(node)

        return size

    collect(self.Root)

    return result

SimpleTree.EvenTrees = EvenTrees
