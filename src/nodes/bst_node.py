from typing import Generic, Iterable, TypeVar, Optional


T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        self.left = None
        self.right = None
        self.data = value
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        ...

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """

        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right


#    @property
    def height(self) -> int:
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 1

    def length(self) -> int:
        if self.left and self.right:
            print ("both")
            return 1 + self.left.length() +  self.right.length()
        elif self.left:
            print ("left")
            return 1 + self.left.length()
        elif self.right:
            print ("right")
            print ("node", self.data)
            return 1 + self.right.length()
        else:
            return 1

    def get_max_node(self) -> Generic[T]:
        if self.right is None:
            return self
        else:
            get_max_node(self.right)



