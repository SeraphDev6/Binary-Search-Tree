from math import trunc
from Node import Node


class BST:
    def __init__(self, root=None):
        self.root = root

    def add(self,value):
        if not self.root:
            self.root = Node(value)
            return self
        runner = self.root
        while True:
            if value > runner.value:
                if not runner.right:
                    runner.right=Node(value)
                    return self
                runner=runner.right
            else:
                if not runner.left:
                    runner.left = Node(value)
                    return self
                runner=runner.left
        

    def contains(self,value):
        runner = self.root
        while runner:
            if value == runner.value:
                return True
            if runner.value < value:
                if runner.right:
                    runner=runner.right
                else:
                    return False
            else:
                if runner.left:
                    runner=runner.left
                else:
                    return False
        return False

    def min(self):
        if self.is_empty():
            return "Tree is empty"
        runner = self.root
        while runner.left:
            runner= runner.left
        return runner.value

    def max(self):
        if self.is_empty():
            return "Tree is empty"
        runner = self.root
        while runner.right:
            runner= runner.right
        return runner.value

    def size(self):
        if self.is_empty():
            return 0
        size = 1 + BST(self.root.left).size() + BST(self.root.right).size()
        return size

    def listify(self):
        if self.is_empty():
            return []
        print("blarg")
        return BST(self.root.left).listify()+[self.root.value]+BST(self.root.right).listify()

    def is_empty(self):
        return self.root == None