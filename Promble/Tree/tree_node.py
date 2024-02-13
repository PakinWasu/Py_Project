class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.data = data
        self.right = None
    def insert(self,data):
        if self.data :
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
    def findval(self,lkpval):
        if lkpval < self.data:
            if self.left is Node:
                return str()
    def DelTree(self,data):
        if (self.left is None )and (self.right is None):
            self.data = None





root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)

root.PrintTree()
root.DelTree(5)
root.PrintTree()
