from Node import Node


class BST:
    def __init__(self, root=None):
        self.root = root

    def add(self,node):
        if not self.root:
            self.root = node
            return
        runner = self.root
        while True:
            if node.value > runner.value:
                if not runner.right:
                    runner.right=node
                    return
                runner=runner.right
            else:
                if not runner.left:
                    runner.left = node
                    return
                runner=runner.left

    def contains(self,value):
        if self.is_empty():
            return False
        runner = self.root
        while runner.value != value:
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
        return True

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
        print("blarg")
        size = 1 + BST(self.root.left).size() + BST(self.root.right).size()
        return size

    def is_empty(self):
        return self.root == None