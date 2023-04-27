class TreeNode:
    def __init__(self, value):
        self.data = value
        self.children = []

    def addChild(self, Node):
        self.children.append(Node)

    def __str__(self, level=0):
        ret = " "*level+str(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level=level+1)
        return ret


Drinks = TreeNode("DRINKS")
Cold = TreeNode("Cold")
Hot = TreeNode("Hot")
Drinks.addChild(Cold)
Drinks.addChild(Hot)
print(Drinks)
