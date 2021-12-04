from BST import BST
from Node import Node
from random import randint
if __name__ == "__main__":
    bst = BST()
    for i in range(20,10,-1):
        bst.add(Node(i))
    print (bst.contains(10))
    print(bst.size())