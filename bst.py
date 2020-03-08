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
    print ("Tree height:", tree.height())
    print ("Tree length:", len(tree))
    node_min = tree.get_min_node()
    print ("Tree min:", node_min.value) 
    node_max = tree.get_max_node()
    print ("Tree max:", node_max.value)
    node_45 = tree.get_node(45)
    print ("Tree 45", node_45.value)
    node_50 = tree.get_node(50)
    print ("Tree 50", node_50.value)
    new_tree = BST()
    new_tree.add_value(100)
    new_tree.add_value(75)
    new_tree.add_value(200)
    new_tree.add_value(300)
    new_tree.add_value(30)
    new_tree.add_value(30)
    new_tree.add_value(30)
    print ("Tree height:", new_tree.height())
    print ("Tree length:", len(new_tree))

    print ("new_tree added value")
    node_100 = new_tree.get_node(100)
    node_100 = new_tree.get_node(30)

    print ("new_tree 100", node_100.value)
    print ("new_tree 75", new_tree.get_node(75).value)
