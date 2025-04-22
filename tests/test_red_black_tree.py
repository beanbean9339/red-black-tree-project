import unittest
from src.red_black_tree import RedBlackTree

class TestRedBlackTree(unittest.TestCase):

    def setUp(self):
        self.tree = RedBlackTree()

    def test_insertion(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.tree.insert(30)
        self.assertIsNotNone(self.tree.search(10))
        self.assertIsNotNone(self.tree.search(20))
        self.assertIsNotNone(self.tree.search(30))
        self.assertIsNone(self.tree.search(40))

    def test_search(self):
        keys = [7, 3, 18, 10, 22, 8, 11, 26]
        for key in keys:
            self.tree.insert(key)
        
        for key in keys:
            self.assertIsNotNone(self.tree.search(key))
        
        self.assertIsNone(self.tree.search(100))
        self.assertIsNone(self.tree.search(-5))

    def test_deletion(self):
        keys = [7, 3, 18, 10, 22, 8, 11, 26]
        for key in keys:
            self.tree.insert(key)
        
        self.tree.delete(18)
        self.tree.delete(11)
        self.tree.delete(3)

        self.assertIsNone(self.tree.search(18))
        self.assertIsNone(self.tree.search(11))
        self.assertIsNone(self.tree.search(3))

        self.assertIsNotNone(self.tree.search(7))
        self.assertIsNotNone(self.tree.search(8))

    def test_traversal(self):
        keys = [20, 15, 25, 10, 18, 22, 30]
        for key in keys:
            self.tree.insert(key)

        traversal_result = []
        self.tree.inorder_traversal(self.tree.root, traversal_result)
        expected_result = sorted(keys)

        self.assertEqual(traversal_result, expected_result)

if __name__ == "__main__":
    unittest.main()
#     def inorder_traversal(self, node, result):
#         if node != self.NIL:
#             self.inorder_traversal(node.left, result)
#             result.append(node.data)
#             self.inorder_traversal(node.right, result)
# 
#     def delete(self, data):
#         # Deletion logic goes here (not implemented in this example)
#         pass