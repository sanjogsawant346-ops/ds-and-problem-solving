import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addNodeBeggining(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addNodeinBetween(self,index, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head - node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node


    def addNodeatEnd(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def displayNode(self):
        print("------------------------")
        while self.head is not None:
          print("|",self.head.data,"|","===>",end=" ")
          self.head=self.head.next
        print("------------------------")

    def searchNode(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return print("Node search successfully")
            current = current.next
        return print("node is not found")

    

#link list add,del,
if __name__ =='__main__':
    object = Linkedlist()

    while True:
        print("1. Add node linkedlist:")
        print("2. Add node in begining:")
        print("3. Add node in between:")
        print("4. Add node in end:")
        print("5. Display linkedlist:")
        print("6. Search Node:")
        print("7.exit")

        ch = int(input("Enter your choice:"))
        if ch == 1:
            value = int(input("enter value for node:"))
            object.addNode(value)
            print("node added successfully insingle linkedlist")

        elif ch == 2:
            value = int(input("enter value for node:"))
            object.addNodeBeggining(value)
            print("node added successfully insingle linkedlist")

        elif ch == 3:
            value = int(input("enter value for node:"))
            index = int(input("enter position after that you have to insert"))
            object.addNodeinBetween(index,value)
            print("node added successfully insingle linkedlist")


        elif ch == 4:
            value = int(input("enter value for node:"))
            object.addNodeatEnd(value)
            print("node added successfully insingle linkedlist")



        elif ch == 5:
            object.displayNode()

        elif ch == 6:
            value = int(input("enter value for node:"))
            object.searchNode(value)
            


        elif ch == 7:
            sys.exit()

        else:
            print("Invalid choice")