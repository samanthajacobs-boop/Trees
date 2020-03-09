import unittest
from typing import Optional, Callable, TypeVar, Generic
from Trees.src.errors import EmptyTreeError, MissingValueError
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')

class TestBST(unittest.TestCase):
    def test_create_empty_tree(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)

    def test_create_tree(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)


    def test_tree_not_eq(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)

    def test_max(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(tree.get_max_node().value, 100)
        tree.add_value(80)
        self.assertEqual(tree.get_max_node().value, 100)
        tree.add_value(200)
        self.assertEqual(tree.get_max_node().value, 200)
        tree.add_value(0)
        self.assertEqual(tree.get_max_node().value, 200)
        tree.add_value(-3)
        self.assertEqual(tree.get_max_node().value, 200)

    
    def test_max_empty(self):
        tree = BST()
        with self.assertRaises(EmptyTreeError):
            tree.get_max_node()


    def test_min_test(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(tree.get_min_node().value, 100)
        tree.add_value(80)
        self.assertEqual(tree.get_min_node().value, 80)
        tree.add_value(200)
        self.assertEqual(tree.get_min_node().value, 80)
        tree.add_value(60)
        self.assertEqual(tree.get_min_node().value, 60)
        tree.add_value(90)
        self.assertEqual(tree.get_min_node().value, 60)
        tree.add_value(0)
        self.assertEqual(tree.get_min_node().value, 0)
        tree.add_value(-1)
        self.assertEqual(tree.get_min_node().value, -1)
        tree.add_value(-3)
        self.assertEqual(tree.get_min_node().value, -3)

    def test_min_empty(self):
        tree = BST()
        with self.assertRaises(EmptyTreeError):
            tree.get_min_node()

    def test_length(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(len(tree), 1)
        tree.add_value(80)
        self.assertEqual(len(tree), 2)
        tree.add_value(200)
        self.assertEqual(len(tree), 3)
        tree.add_value(60)
        self.assertEqual(len(tree), 4)
        tree.add_value(90)
        self.assertEqual(len(tree), 5)
        tree.add_value(0)
        self.assertEqual(len(tree), 6)
        tree.add_value(-3)
        self.assertEqual(len(tree), 7)
        tree.add_value(-2)
        self.assertEqual(len(tree), 8)

    def test_empty_length(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        

    def test_height(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(tree.height(), 1)
        tree.add_value(80)
        self.assertEqual(tree.height(), 2)
        tree.add_value(200)
        self.assertEqual(tree.height(), 2)
        tree.add_value(60)
        self.assertEqual(tree.height(), 3)
        tree.add_value(90)
        self.assertEqual(tree.height(), 3)
        tree.add_value(0)
        self.assertEqual(tree.height(), 4)
        tree.add_value(-3)
        self.assertEqual(tree.height(), 5)
        tree.add_value(1)
        self.assertEqual(tree.height(), 5)
    
    def test_empty_height(self):
        tree = BST()
        self.assertEqual(tree.height(), -1)


    def test_get_node(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(tree.get_node(100).value, 100)
        tree.add_value(80)
        self.assertEqual(tree.get_node(80).value, 80)
        tree.add_value(200)
        self.assertEqual(tree.get_node(200).value, 200)
        tree.add_value(60)
        self.assertEqual(tree.get_node(60).value, 60)
        tree.add_value(90)
        self.assertEqual(tree.get_node(90).value, 90)
        tree.add_value(0)
        self.assertEqual(tree.get_node(0).value, 0)
        tree.add_value(-3)
        self.assertEqual(tree.get_node(-3).value, -3)
        tree.add_value(1)
        self.assertEqual(tree.get_node(1).value, 1)
        

    def test_get_node_empty(self):
        tree = BST()
        with self.assertRaises(EmptyTreeError):
            tree.get_node(100)

    def test_add_value(self):
        tree = BST()
        tree.add_value(100)
        self.assertEqual(tree.get_node(100).value, 100)
        self.assertEqual(len(tree), 1)

    def test_get_node_not_equal(self):
        tree = BST()
        tree.add_value(100)
        with self.assertRaises(MissingValueError):
            tree.get_node(90)

    def test_init_(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x:x) -> None:
        node = BSTNode(45)
        tree = BST(node)
        self.assertEqual(tree.get_node(45).value, 45)

    def test_remove_leaf(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        
        tree.remove_value(70)
        results = []
        values = []
        tree.inorder(results)
        
        for x in results:
            value = x.value
            values.append(value)

        self.assertEqual(values, [80, 90, 100, 200])
    
    def test_remove_empty(self):
        tree = BST()
        with self.assertRaises(EmptyTreeError):
            tree.remove_value(70)

    def test_remove_right_child(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(150)

        tree.remove_value(200)
        results = []
        values = []
        tree.inorder(results)

        for x in results:
            value = x.value
            values.append(value)

        self.assertEqual(values, [70, 80, 90, 100, 150])
    

    def test_remove_left_child(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        tree.remove_value(200)
        results = []
        values = []
        tree.inorder(results)

        for x in results:
            value = x.value
            values.append(value)

        self.assertEqual(values, [70, 80, 90, 100])
    

    def test_remove_both_children(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)
        tree.add_value(150)

        tree.remove_value(80)
        results = []
        values = []
        tree.inorder(results)

        for x in results:
            value = x.value
            values.append(value)

        self.assertEqual(values, [70, 90, 100, 150, 200])


if __name__ == '__main__':
    unittest.main()
