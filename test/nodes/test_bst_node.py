import unittest



class TestBSTNode(unittest.TestCase):
    def test_add_node_with_children(self):
        tree = BST()
        a = BSTNode(50)
        b = BSTNode(40)
        c = BSTNode(35)
        d = BSTNode(37)
        e = BSTNode(45)
        f = BSTNode(90)
        g = BSTNode(150)

        a.left = b
        b.left = c
        c.right = d
        b.right = e

        m =BSTNode(45, children = [a])

        results = []
        self.AssertEqual(len(tree), 6)

    def test_add_node_with_two_children(self):
        tree1 = BST(m)
        a = BSTNode(50)
        b = BSTNode(40)
        c = BSTNode(35)
        d = BSTNode(37)
        e = BSTNode(45)
        f = BSTNode(90)
        g = BSTNode(150)

        a.left = b
        b.left = c
        c.right = d
        b.right = e

        results = []
        m = BSTNode(65, chilren = [a,f])
        self.AssertEqual(len(tree1), 7)

    def test_add_parent(self):
        p = BSTNode(200)
        n = BSTNode(75, children = [m, g], parent = p)
        tree2 = BST(p)
        a = BSTNode(50)
        b = BSTNode(40)
        c = BSTNode(35)
        d = BSTNode(37)
        e = BSTNode(45)
        f = BSTNode(90)
        g = BSTNode(150)

        a.left = b
        b.left = c
        c.right = d
        b.right = e

        results = []
        self.AssertEqual(len(tree2), 10)


if __name__ == '__main__':
    unittest.main()
