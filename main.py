from BST import BST
from Node import Node
from random import randint
if __name__ == "__main__":
    bst = BST()
    for i in range(50):
        bst.add(randint(1,100))
    print(bst.listify())
    print (bst.contains(12))