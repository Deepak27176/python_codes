class BstNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, node_value):
        if self.data is None:

            self.data = node_value

        elif self.data >= node_value:

            if self.left is None:
                self.left = BstNode(node_value)
            else:
                self.left.insert_node(node_value)
        else:
            if self.right is None:
                self.right = BstNode(node_value)
            else:
                self.right.insert_node(node_value)

    def search_node(self, root_node, value):
        if root_node.data is None:
            return
        if root_node.data == value:
            return True
        elif value < root_node.data:
            if root_node.left:
                return self.search_node(root_node.left, value)
        else:
            if root_node.right:
                return self.search_node(root_node.right, value)
        return False

    def min_value_node(self,bstNode):
        current = bstNode
        while (current.left is not None):
            current = current.left
        return current

    def postorder_traversal(self,root):
        if not root:
            return
        if root.left:
            root.left.postorder_traversal(root.left)
        if root.right:
            root.right.postorder_traversal(root.right)
        print(root.data)

    def delete_node(self, root, value):
        if not root:
            return
        elif value < root.data:
            root.left = self.delete_node(root.left, value)

        elif value > root.data:
            root.right = self.delete_node(root.right, value)
        else:
            if root.right is None:
                temp = root.left
                root = None
                return temp
            if root.left is None:
                temp = root.right
                root = None
                return temp
        temp = self.min_value_node(root.right)

        root.data = temp.data

        root.right = root.right.delete_node(root.right, temp.data)


newBst = BstNode(None)
newBst.insert_node(70)
newBst.insert_node(60)
newBst.insert_node(63)
newBst.insert_node(90)
# newBst.insert_node(newBst, 30)
# newBst.insert_node(newBst, 20)
# newBst.insert_node(newBst, 163)
newBst.insert_node(98)
# newBst.delete_node(70)
newBst.postorder_traversal(newBst)


