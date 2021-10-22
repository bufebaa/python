from __future__ import print_function
from collections import deque


class Product:
    def __init__(self, id, name,price, quantity) :
        if not isinstance(id, int): raise TypeError
        self.Id = id
        if not isinstance(name, str): raise TypeError
        self.name = name
        if not isinstance(price, float): raise TypeError
        if not price >= 0 : raise TypeError
        self.price = price
        if not isinstance(quantity, int): raise TypeError
        self.quantity = quantity

    def get_name(self):
        return self.__name
    @property
    def name(self):
         return self.__name
    @name.setter
    def name(self, name):
        if not isinstance(name, str): raise TypeError
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, float): raise TypeError
        if price < 0: raise ValueError
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int): raise TypeError
        self.__quantity = quantity

    def __str__(self):
        return f"Id: {self.Id} | Name: {self.name} | Price: {self.price}"


class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        #Added in order to delete a node easier
        self.parent = parent

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getTotalValue(self):
        return str(self.label.price*self.label.quantity)

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label : Product):
        # Create a new Node
        new_node = Node(label, None)
        # If Tree is empty
        if self.empty():
            self.root = new_node
        else:
            #If Tree is not empty
            curr_node = self.root
            #While we don't get to a leaf
            while curr_node is not None:
                #We keep reference of the parent node
                parent_node = curr_node
                #If node label is less than current node
                if new_node.getLabel().Id < curr_node.getLabel().Id:
                #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
            #We insert the new node in a leaf
            if new_node.getLabel().Id < parent_node.getLabel().Id:
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            #Set parent to the new node
            new_node.setParent(parent_node)

    def delete(self, label : Product):
        if (not self.empty()):
            #Look for the node with that label
            node = self.getNode(label)
            #If the node exists
            if(node is not None):
                #If it has no children
                if(node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                #Has only right children
                elif(node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                #Has only left children
                elif(node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                #Has two children
                else:
                    #Gets the max value of the left branch
                    tmpNode = self.getMax(node.getLeft())
                    #Deletes the tmpNode
                    self.delete(tmpNode.getLabel())
                    #Assigns the value to the node to delete and keesp tree structure
                    node.setLabel(tmpNode.getLabel())

    def getNode(self, label):
        curr_node = None
        if(not self.empty()):
            curr_node = self.getRoot()
            while curr_node is not None and curr_node.getLabel() is not label:
                #If node label is less than current node
                if label.Id < curr_node.getLabel().Id:
                    #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if(not self.empty()):
            while(curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root = None):
        if(root is not None):
            curr_node = root
        else:
            curr_node = self.getRoot()
        if(not self.empty()):
            curr_node = self.getRoot()
            while(curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def getRoot(self):
        return self.root

    def __isRightChildren(self, node):
        if(node == node.getParent().getRight()):
            return True
        return False

    def __reassignNodes(self, node, newChildren):
        if(newChildren is not None):
            newChildren.setParent(node.getParent())
        if(node.getParent() is not None):
            if(self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                node.getParent().setLeft(newChildren)

    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()+"| Total Value: "+x.getTotalValue()+"\n"
        return str

def InPreOrder(curr_node):
    nodeList = []
    if curr_node is not None:
        nodeList = nodeList + InPreOrder(curr_node.getLeft())
        nodeList.insert(0, curr_node.getLabel())
        nodeList = nodeList + InPreOrder(curr_node.getRight())
    return nodeList


prod1 = Product(8, "Hat", 10.0, 8)
prod2 = Product(3, "Hat", 74.0, 7)
prod3 = Product(10, "Hat", 65.0, 6)
prod4 = Product(1, "Hat", 65.0, 9)
prod5 = Product(6, "Hat", 65.0, 2)
prod6 = Product(14, "Hat", 65.0, 8)
prod7 = Product(4, "Hat", 65.0, 9)
prod8 = Product(7, "Hat", 65.0, 8)
prod9 = Product(13, "Hat", 65.0, 8)


tree = BinarySearchTree()
tree.insert(prod1)
tree.insert(prod2)
tree.insert(prod3)
tree.insert(prod4)
tree.insert(prod5)
tree.insert(prod6)
tree.insert(prod7)
tree.insert(prod8)
tree.insert(prod9)
tree.delete(prod2)
print(tree)
print("\n")
