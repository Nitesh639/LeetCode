class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    lastNode.next = newNode
                    break
                lastNode = lastNode.next

    def listLength(self):
        currentNode = self.head
        length = 0
        while True:
            length += 1
            if currentNode.next is None:
                return length
            currentNode = currentNode.next

    def insertAt(self, newNode, posion):
        if posion < 0 or self.listLength() < posion:
            print("Operation will work")
            return
        if posion == 0:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            del temp
            return
        currentNode = self.head
        currentPos = 0
        while True:
            if currentPos == posion:
                pre.next = newNode
                newNode.next = currentNode
                return
            pre = currentNode
            currentNode = currentNode.next
            currentPos = currentPos + 1

    def printList(self):
        currentNode = self.head
        while True:
            print(currentNode.data)
            print(currentNode.next)
            if currentNode.next is None:
                break
            currentNode = currentNode.next


firstNo = Node(1)
linkedlist = LinkedList()
linkedlist.insert(firstNo)
secNo = Node(11)
linkedlist.insert(secNo)
firstN1o = Node(12)
firstNo1 = Node(13)
theNo = Node(23)
linkedlist.insertAt(theNo, 10)

linkedlist.insert(firstN1o)
linkedlist.insert(firstNo1)

linkedlist.printList()
x = linkedlist.listLength()
print(x)
