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
        """
        :return: the number of nodes in the tree
        """
        if self.root is None:
            return 0
        else:
            return self.root.length()
        
        #def bst_insert(value: T, root: Node[T])-> Node[T]:
        

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        :param value:
        :return:
        """
        if self.root:
            return self.insert_recurse(value, self.root)
        else:
            self.root = BSTNode(value)
            return

    def insert_recurse(self, value: T, node: BSTNode[T]) -> BSTNode[T]:
        #if node.value == value:
        #    return   # come back and allow dups
        #elif node.value > value:
        if node.value >= value:
            if node.left:
                return self.insert_recurse(value,node.left)
            else:
                node.left = BSTNode(value)
                return

        else:
            if node.right:
                return self.insert_recurse(value,node.right)
            else:
                node.right = BSTNode(value)
                return

    def get_node(self, value: K) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        if self.root is None:
            raise EmptyTreeError()
        else:
            return self.get_node_recurse(value, self.root)


    def get_node_recurse(self, value: K,node: BSTNode[T]) -> BSTNode[T]:    
        try:
            value == node.value
        except:
            raise MissingValueError()
        if value == node.value:
            return node
        elif value < node.value:
            return self.get_node_recurse(value, node.left)
        else:
            return self.get_node_recurse(value, node.right)
        

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        if self.root is None:
            raise EmptyTreeError()
        else:
            return self.get_max_node_recurse(self.root)

    def get_max_node_recurse(self, node: BSTNode[T]) -> BSTNode[T]:
        if node.right is None:
            return node
        else:
            return self.get_max_node_recurse(node.right)

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        if self.root is None:
            raise EmptyTreeError()
        else:
            return self.get_min_node_recurse(self.root)

    def get_min_node_recurse(self, node: BSTNode[T]) -> BSTNode[T]:
        if node.left is None:
            return node
        else:
            return self.get_min_node_recurse(node.left)


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
