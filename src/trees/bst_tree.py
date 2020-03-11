from typing import Optional, Callable, TypeVar, Generic, List


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
        self.key = key
        self.bst_length = self.len_via_tree(root)

    #@property
    def height(self) -> int:
        if self.root:
            return self.height_recurse(self.root) -1
        else:
            return -1
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
    def height_recurse(self, node: BSTNode[T]) -> int:
        if node.left and node.right:
            return 1 + max(self.height_recurse(node.left), self.height_recurse(node.right))
        elif node.left:
            return 1 + self.height_recurse(node.left)
        elif node.right:
            return 1 + self.height_recurse(node.right)
        else:
            return 1
        
    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        return self.bst_length

#    def __len__(self) -> int:
#        """
#        :return: the number of nodes in the tree
#        """
#        if self.root is None:
#            return 0
#        else:
#            return self.length(self.root)

    def len_via_tree(self,root: BSTNode[T]) -> int:
        """
        :return: the number of nodes in the tree
        """
        if root is None:
            return 0
        else:
            return self.length(root)

    def length(self, node: BSTNode[T]) -> int:
        if node.left and node.right:
            return 1 + self.length(node.left) +  self.length(node.right)
        elif node.left:
            return 1 + self.length(node.left)
        elif node.right:
            return 1 + self.length(node.right)
        else:
            return 1
        

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        :param value:
        :return:
        """
        self.bst_length += 1
        if self.root:
            return self.insert_recurse(value, self.root,self.key)
        else:
            self.root = BSTNode(value)
            return

    def insert_recurse(self, value: T, node: BSTNode[T], key: Callable[[T], K]) -> BSTNode[T]:
        #if node.value == value:
        #    return   # come back and allow dups
        #elif node.value > value:
        if key(node.value) > key(value):
            if node.left:
                return self.insert_recurse(value,node.left,key)
            else:
                node.left = BSTNode(value)
                return

        else:
            if node.right:
                return self.insert_recurse(value,node.right,key)
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
            return self.get_node_recurse(value, self.root,self.key)


    def get_node_recurse(self, value: K,node: BSTNode[T],key: Callable[[T], K]) -> BSTNode[T]:    
        try:
            value == key(node.value)
        except:
            raise MissingValueError()
        if value == key(node.value):
            return node
        elif value < key(node.value):
            return self.get_node_recurse(value, node.left,key)
        else:
            return self.get_node_recurse(value, node.right,key)
        

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


    def remove_value(self, value: K) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        self.remove_value_helper(value,self.key)
        return


    def remove_value_helper(self, value: K, key: Callable[[T], K]) -> None:
        if self.root is None:
            raise EmptyTreeError()
        elif key(self.root.value) == value:     # matches parent
            self.bst_length -= 1
            return
        parent = None
        node = self.root
        # find node to remove
        while node and key(node.value) != value:
            parent = node
            if value < key(node.value):
                node = node.left
            elif value > key(node.value):
                node = node.right

        # if not found has error
        if node is None or key(node.value) != value:
            raise MissingValueError()
        
        # easy case, no children
        elif node.left is None and node.right is None:
            self.bst_length -= 1
            if value < key(parent.value):
                parent.left = None
            else:
                parent.right = None
            return

        # left node only
        elif node.left and node.right is None:
            self.bst_length -= 1
            if value < key(parent.value):
                parent.left = node.left
            else:
                parent.right = node.left
            return

        # right node only
        elif node.left is None and node.right:
            self.bst_length -= 1
            if value < key(parent.value):
                parent.left = node.right
            else:
                parent.right = node.right
            return

        # both children exist
        else:
            self.bst_length -= 1
            delNodeParent = node
            delNode = node.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left
		
            node.value = delNode.value
            if delNode.right:
                if key(delNodeParent.value) > key(delNode.value):
                    delNodeParent.left = delNode.right
                elif key(delNodeParent.value) < key(delNode.value):
                    delNodeParent.right = delNode.right
            else:
                if key(delNode.value) < key(delNodeParent.value):
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None

#########################  end remove #######################

    def inorder(self,results: List[BSTNode[T]]) -> None:
        if self.root is None:
            raise EmptyTreeError()
        else:
            return self.inorder_recurse(self.root, results)

    def inorder_recurse(self, node: BSTNode[T], results: List[BSTNode[T]]) -> BSTNode[T]:
        if node.left:
            self.inorder_recurse(node.left,results)
        #print (node.value)
        results.append(node)
        if node.right:
            self.inorder_recurse(node.right, results)
       

 

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
