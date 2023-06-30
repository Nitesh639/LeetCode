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
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("Empty LinkedList")
            return
        currentNode = self.head
        while True:
            print(currentNode.data)
            if currentNode.next is None:
                break
            currentNode = currentNode.next

    def headInsert(self, newNode):
        temp = self.head
        self.head = newNode
        self.head.next = temp

        del temp


firstNode = Node("Nitesh")
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node("Kumar")
linkedlist.insert(secondNode)
thirdNode = Node("Kushwaha")
fstNode = Node(4)
linkedlist.insert(thirdNode)
linkedlist.headInsert(fstNode)
linkedlist.printList()
