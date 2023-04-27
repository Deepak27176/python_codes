class Binarytree:
    def __init__(self, size):
        self.tree_list = [None]*size
        self.used_index = 0
        self.maxSize = size
        print("Tree Created")

    def add_node(self, data):
        if self.used_index + 1 == self.maxSize:
            return "Binary Tree list is empty"
        else:
            self.tree_list[self.used_index+1] = data
            self.used_index += 1
            return "successfully inserted"

    def print_tree(self):
        for i in self.tree_list[1:self.used_index+1]:
            print(i)

    def pre_order(self, index):
        if index > self.used_index:
            return
        print(self.tree_list[index])
        self.pre_order(index*2)
        self.pre_order(index*2+1)

    def inorder(self, index):
        if index > self.used_index:
            return
        self.inorder(index*2)
        print(self.tree_list[index])
        self.inorder(index*2+1)

    def post_order(self, index):
        if index > self.used_index:
            return
        self.post_order(index*2)
        self.post_order(index*2 + 1)
        print(self.tree_list[index])

    def delete_node(self, data):
        deepest = self.tree_list[self.used_index]
        self.tree_list[self.used_index] = None
        self.used_index -= 1

        for index in range(len(self.tree_list)):
            if self.tree_list[index] == data:
                self.tree_list[index] = deepest
                return


BT = Binarytree(9)
BT.add_node("Drinks")
BT.add_node("Hot")
BT.add_node("Cold")
BT.add_node("Tea")
BT.add_node("Coffee")
BT.add_node("Cola")
BT.add_node("Pepsi")
BT.print_tree()
# BT.pre_order(1)
print("\n")
# BT.inorder(1)
# BT.post_order(1)
BT.delete_node("Cold")
BT.print_tree()
