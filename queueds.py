# import sys
# class Queue:
  
#   def __init__(self,queueSize): #parameterized constructor
#     self.queueList = [] #stack created
#     self.queueSize = queueSize
  
#   def isFull(self):
#       if len(self.queueList) == self.queueSize:
#           return True
#       else:
#           return False

#   def Enqueue(self, value):
#     if self.isFull():
#       print("Queue is full")
#     else:
#       self.queueList.append(value)
#       print(self.queueList)

#   def displayQueue(self):
#     print("------------------")
#     print(self.queueList)
#     print("------------------")

#   def isEmpty(self):
#         if self.queueList == []:
#                 return True
#         else:
#                 return False
             
#   def Dequeue(self):
#       if self.isEmpty():
#           return "Queue is empty"
#       else:
#           return self.queueList.pop(0)

#   def deleteQueue(self):
#       self.queueList = None
#       return "Queue is deleted"
   
#   def peek(self):
#       if self.isEmpty():
#           return "Queue is empty"
#       else:
#           return self.queueList[0]
      
# size = int(input("enter the size of queue :"))
# queueObj = Queue(size)

# while True:
  
#   print("1. enqueue element in queue :")
#   print("2. display queue element :")
#   print("3.check Queue isempty :")
#   print("4.dequeue operation :")
#   print("5.delete queue :")
#   print("6.peek operation :")
#   print("7. exit")

#   choice = int(input("enter your choice : "))
#   if choice == 1:
#     val = int(input("enter value for queue :"))
#     queueObj.Enqueue(val)

#   elif choice == 2:
#     queueObj.displayQueue()
  
#   elif choice == 3:
#       print(queueObj.isEmpty())

#   elif choice == 4:
#       print(queueObj.Dequeue())
 
#   elif choice == 5:
#       print(queueObj.deleteQueue())

#   elif choice == 6:
#       print(queueObj.peek())
  
#   elif choice == 7:
#       sys.exit()


