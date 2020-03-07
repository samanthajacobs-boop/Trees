from Trees.src.nodes.bst_node import BSTNode
from Trees.src.trees.bst_tree import BST

if __name__ == '__main__':
    a = BSTNode(50)
    b = BSTNode(40)
    c = BSTNode(35)
    d = BSTNode(37)
    e = BSTNode(45)

    a.left = b
    b.left = c 
    c.right = d
    b.right = e

    tree = BST(a)
    tree2 = BST()
    print ("tree2", tree2 )
    print ("Node d:", d.data, d.right )
    print ("Tree height:", tree.height())
    print ("Tree length:", len(tree))
    node = tree.get_max_node()
    print ("Tree max:", node.data)
    

