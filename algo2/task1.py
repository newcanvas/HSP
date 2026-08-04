class SimpleTreeNode:
	
    def __init__(self, val, parent):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild) -> None:
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
        return

    def DeleteNode(self, NodeToDelete) -> None:
        if NodeToDelete.Parent is None:
            self.Root = None
            return
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        return

    def GetAllNodes(self) -> list:
        all_nodes = []
        self._get_all_nodes_rec(self.Root, all_nodes)
        return all_nodes

    def _get_all_nodes_rec(self, node, all_nodes) -> list:
        if node is None:
            return
        
        all_nodes.append(node)

        for child in node.Children:
            self._get_all_nodes_rec(child, all_nodes)

        return all_nodes

    def FindNodesByValue(self, val) -> list:
        all_nodes_by_value = []
        self._find_nodes_by_value_rec(self.Root, val, all_nodes_by_value)
        return all_nodes_by_value

    def _find_nodes_by_value_rec(self, node, val, all_nodes_by_value) -> list:
        if node is None:
            return
        
        if node.NodeValue == val:
            all_nodes_by_value.append(node)

        for child in node.Children:
            self._find_nodes_by_value_rec(child, val, all_nodes_by_value)

        return all_nodes_by_value
   
    def MoveNode(self, OriginalNode, NewParent) -> None:
        if OriginalNode == self.Root:
            return
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
   
    def Count(self) -> int:
        all_nodes = []
        self._get_all_nodes_rec(self.Root, all_nodes)
        return len(all_nodes)

    def LeafCount(self) -> int:
        all_leaves = []
        self._count_leaves(self.Root, all_leaves)
        return len(all_leaves)
    
    def _count_leaves(self, node, all_leaves) -> int:
        if node is None:
            return
        
        if node.Children == []:
            all_leaves.append(node)

        for child in node.Children:
            self._count_leaves(child, all_leaves)

        return all_leaves
