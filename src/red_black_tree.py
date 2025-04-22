class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'RED'  # New nodes are RED
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 'BLACK'
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'RED'

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 'BLACK'
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 'RED':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle
                if u.color == 'RED':
                    # Case 1: uncle is RED
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Case 2: k is left child
                        k = k.parent
                        self.right_rotate(k)
                    # Case 3: k is right child
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Uncle

                if u.color == 'RED':
                    # Mirror Case 1
                    u.color = 'BLACK'
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent 
                else:
                    if k == k.parent.right:
                        # Mirror Case 2
                        k = k.parent
                        self.left_rotate(k)
                    # Mirror Case 3
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'BLACK'

    def search(self, key):
        return self._search_tree_helper(self.root, key)

    def _search_tree_helper(self, node, key):
        if node == self.NIL or key == node.data:
            return node

        if key < node.data:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    def in_order_traversal(self):
        self._in_order_helper(self.root)
        print()

    def _in_order_helper(self, node):
        if node != self.NIL:
            self._in_order_helper(node.left)
            print(node.data, end=' ')
            self._in_order_helper(node.right)
