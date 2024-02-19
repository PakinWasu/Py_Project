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
            if self.left is None:
                return str(lkpval)+'Not Found'
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+' Not Found'        
            return self.right.findval(lkpval) 
        else:
            return str(self.data)+' is found'
    def InorderTraversal(self,root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            if root.data is not None:
                res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res
    def PreorderTraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    def PostorderTraversal(self,root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res
    def delete(self, data):
        if data < self.data and self.left.data != data:
            self.left.delete(data)
        elif data > self.data and self.right.data != data:
            self.right.delete(data)
        else :
            if data == self.right.data: # del node right
                if self.right.right is not None and self.right.left is not None:
                    if self.right.right.left is None:
                        RR = self.right.right
                        LL = self.right.left
                        self.right = None
                        self.right = RR
                        self.right.left = LL
                    elif self.right.right.left is not None:
                        RR = self.right.right
                        LL = self.right.left
                        self.right = None
                        lest_rr = RR
                        while lest_rr.left is not None:
                            lest_rr = lest_rr.left
                        self.right = lest_rr
                        RR.delete(lest_rr.data)
                        self.right.right = RR
                        self.right.left =LL
                elif self.right.right is None and self.right.left is not None:#กรณี 2
                    left = self.right.left
                    self.right = None
                    self.right = left
                elif self.right.right is not None and self.right.left is None:#กรณี 2
                    right = self.right.right 
                    self.right = None
                    self.right = right
                elif self.right.right is not None and self.right.left is not None:
                    self.right.right.left
                elif self.right.right is None and self.right.left is None:#กรณี 1
                    self.right = None
            elif data == self.left.data:
                if self.left.right is not None and self.left.left is not None:
                    if self.left.right.left is None:
                        RR = self.left.right
                        LL = self.left.left
                        self.left = None
                        self.left = RR
                        self.left.left = LL
                    elif self.left.right.left is not None:
                        RR = self.left.right
                        LL = self.left.left
                        self.left = None
                        lest_rr = RR
                        while lest_rr.left is not None:
                            lest_rr = lest_rr.left
                        self.left = lest_rr
                        RR.delete(lest_rr.data)
                        self.left.right = RR
                        self.left.left =LL
                elif self.left.right is None and self.left.left is not None:#กรณี 2
                    left = self.left.left
                    self.left = None
                    self.left = left
                elif self.left.right is not None and self.left.left is None:#กรณี 2
                    right = self.left.right 
                    self.left = None
                    self.left = right
                elif self.left.right is None and self .left.left is None:#กรณี 1
                    self.left = None
                    
root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
root.insert(19)
print(root.InorderTraversal(root))
root.delete(30)
print(root.InorderTraversal(root))
