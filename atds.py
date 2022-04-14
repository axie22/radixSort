#1/usr/bin/env python3

"""

DO NOT ADD TO THIS ATDS NOT MEANT TO BE SUBMITTED. USE UNIT4 ATDS
"""

__author__ = "Alex Xie"
__version__ = "2022-02-14"

from http.client import PARTIAL_CONTENT
import re
import time

class Stack(object):

    def __init__(self): #initialize empty stack
        self.stack = []
    
    def push(self, item): #add item to stack at the end
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0: #check if stack is empty
            return None
        else: #return removed item
            return self.stack.pop() #pop() removes from end of list if value is not specified

    def size(self):
        return len(self.stack)

    def isEmpty(self): #returns True is stack is empty
        if len(self.stack) == 0: #check is stack is empty
            return True
        else:
            return False
    
    def peek(self): #returns the last item in the stack
        if len(self.stack) == 0: #check if stack is empty
            return None
        else:
            return self.stack[-1] #retrun the last element of the stack

    def __str__(self): #return a string representation of the stack
        return str(self.stack)
    

class Queue(object):

    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        self.queue.pop(0)
        
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)
    
class Deque(object):
    
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)
    
    def addRear(self, item):
        self.deque.append(item)

    def removeFront(self):
        return self.deque.pop(0)
    
    def removeRear(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)
    
    def isEmpty(self):
        if len(self.deque) == 0:
            return True
        else:
            return False


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next = newNext

    def __str__(self):
        return "Node[data=" + str(self.data) + ", next=" + str(self.next) + "]"

class UnorderedList(object):

    def __init__(self):
        self.head = None
    
    def add(self, data):
        #creates a new node with the new data and adds it to the head of the list
        n = Node(data)
        n.setNext(self.head)
        self.head = n

    def getNext(self):
        #gets the next node in the list
        return self.head.getNext()

    def length(self):
        #returns the length of the list
        count = 0
        if self.head == None:
            return count #if there is no head then the list is empty
        else:
            currentNode = self.head
            while currentNode != None: #while there is still another item in the list
                currentNode = currentNode.getNext()
                count += 1
            return count

    def search(self, data):
        #returns true if item is in the list, false otherwise
        currentNode = self.head
        while currentNode.getData() != data:
            currentNode = currentNode.getNext()
            if currentNode == None:
                return False
        return True
    
    def append(self, item):
        #append an item to the end of the list
        newNode = Node(item)
        currentNode = self.head
        if currentNode == None:
            self.head = newNode
        else:
            while currentNode.getNext() != None:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)

    def isEmpty(self):
        #returns true if the list is empty
        if self.head == None: #if there is no head
            return True
        else:
            return False
    
    def remove(self, data):
        """Go through linked list, find the item, and remove it be resetting next links"""
        currentNode = self.head
        previousNode = None
        
        while currentNode != None:
            if currentNode.getData() == data:
                #problem with removing two items in a row
                if previousNode == None:
                    self.head = currentNode.getNext()
                    currentNode = self.head
                else:
                    previousNode.setNext(currentNode.getNext())
                    currentNode = currentNode.getNext()
            else:
                previousNode = currentNode
                currentNode = currentNode.getNext()

    
    def index(self, data):
        #return the index of the item in the list
        count = 0
        currentNode = self.head
        while currentNode != None:
            if currentNode.getData() == data:
                return count
            else:
                count += 1
                currentNode = currentNode.getNext()
        
        return None
    
    def insert(self, pos, data):
        #assumes the item is not already in the list and that the position exists
        newNode = Node(data)
        previous = None
        current = self.head
        index = 0
        while index != pos:
            previous = current
            current = current.getNext()
            index += 1
        newNode.setNext(current)
        if previous != None:
            previous.setNext(newNode)
        else:
            self.head = newNode
    
    
    def pop(self, position = -1):
        #Removes the item from the given position, or the last item in the list if no position is specified
        previous = None
        currentNode = self.head
        index = 0
        if self.head == None:
            return None
        while index != position and currentNode.getNext() != None:
            previous = currentNode
            currentNode = currentNode.getNext()
            index += 1
        if previous != None:
            previous.setNext(currentNode.getNext())
        else:
            self.head = currentNode.getNext()
        return currentNode.getData()


    def __repr__(self):
        #Creates a representation of the list suitable for printing, debugging. 
        result = "UnorderedList["
        nextNode = self.head
        while nextNode != None:
            result += str(nextNode.getData()) + ","
            nextNode = nextNode.getNext()
        if result[-1] == ",":
            result = result[:-1] # remove trailing comma
        result = result + "]"
        return result

class ULStack(object):

    def __init__(self):
        #create a new empty stack by using an unordered list
        self.ULstack = UnorderedList()
    
    def push(self, item):
        #Pushes an item onto the top of the stack
        self.ULstack.add(item)
    
    def pop(self):
        return self.ULstack.pop(0)
    
    def peek(self):
        if not self.ULstack.isEmpty:
            item = self.ULstack.pop(0)
            self.ULstack.push(item)
            return item
        else:
            return None
    
    def isEmpty(self):
        return self.ULstack.isEmpty()
    
    def size(self):
        return self.ULstack.length()

    def __repr__(self):
        return self.ULstack.__repr__()

class BinaryTree(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def getRootVal(self):
        return self.val
    
    def setRootVal(self, new_val):
        self.val = new_val

    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def insertLeft(self, new_left_child):
        t = BinaryTree(new_left_child) #create a new tree
        t.left = self.left             #set the new tree's left child to the old left child
        self.left = t                  #set the old left child to the new tree
        
    def insertRight(self, new_right_child):
        t = BinaryTree(new_right_child)
        t.right = self.right
        self.right = t
        
    def __str__(self):
        return "BinaryTree[key=" + str(self.val) + \
            ", left_child=" + str(self.left) + \
            ", right_child=" + str(self.right) + "]" 
        

def main():
    uls = ULStack()
    uls.push(1)
    uls.push(2)
    uls.push(3)
    print(uls)
    print(uls.pop())
    print(uls)
    print(uls.peek())
    print(uls.size())
    print(uls.isEmpty())


if __name__ == "__main__":
    main()
