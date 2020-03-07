from typing import Optional, Callable, TypeVar, Generic


#from bstnode import BSTNode
from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.root = root
#        self.data = data
#        self.root.right = root.right
#        self.root.left = root.left
#        ...

    #@property
    def height(self) -> int:
        if self.root:
            return self.root.height()
        else:
            return -1
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        

    def __len__(self) -> int:
        if self.root is None:
            return 0
        else:
            return self.root.length()
        
        """
        :return: the number of nodes in the tree
        """
        

    def add_value(self, value: T) -> None:
        def bst_insert(value: T, root: Node[T])-> Node[T]:
            if root is None:
                return Node(value)
            elif value < root.value:
                root.left = bst_insert(value, root.left)
                root.left.parent = root
            else:
                root.right = bst_insert(value, root.right)
                root.right.parent = root
            return root
        """
        Add value to this BST
        :param value:
        :return:
        """
    

    def get_node(self, value: K) -> BSTNode[T]:
        if root is None:
            raise MissingValueError()
        elif value == self.root.value:
            return root
        elif value < self.root.value:
            return bst_get(value, self.root.left)
        else:
            return bst_get(value, self.root.right)
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        

    def get_max_node(self) -> BSTNode[T]:
        if self.root is None:
            raise MissingValueError()
        else:
            return self.root.get_max_node()       
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """

    def get_min_node(self) -> BSTNode[T]:
        if root is None:
            raise MissingValueError()
        elif root.left is None:
            return root
        else:
            get_min_node(self.root.left)
        """
        Return the node with the smallest value in the BST
        :return:
        """

#    def remove_value(self, value: T) -> None:
#        node_to_remove = bst_get(value, root)
#        if node_to_remove.has_no_children():
#            node_to_remove.parent.remove_child(node_to_remove)
#        elif node_to_remove.num_children == 1:
#            node_to_remove.parent.replace_children(node_to_remove, node_to_remove.left)
#        if node_to_remove.left is not None else node_to_remove.right)
#            else:
#                successor = bst_max(node_to_remove.left)
#                bst_remove(successor.value, successor.parent)
#                node_to_remove.parent.replace_child(node_to_remove, successor)
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
    

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       all((BST(c1) == BST(c2) for c1, c2 in zip(self.root, other.root)))
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)
