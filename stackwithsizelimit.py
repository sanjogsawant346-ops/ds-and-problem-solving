# import sys
# class Stack:
  
#   def __init__(self,stackSize): #parameterized constructor
#     self.stacklist = [] #stack created
#     self.stackSize = stackSize
  
#   def isFull(self):
#       if len(self.stacklist) == self.stackSize:
#           return True
#       else:
#           return False

#   def push(self, value):
#     if self.isFull():
#       print("Stack is full")
#     else:
#       self.stacklist.append(value)
#       print(self.stacklist)

#   def displaystack(self):
#     print(self.stacklist)

#   def isEmpty(self):
#         if self.stacklist == []:
#                 return True
#         else:
#                 return False
             
#   def pop(self):
#       if self.isEmpty():
#           return "Stack is empty"
#       else:
#           return self.stacklist.pop()

#   def deleteStack(self):
#       self.stacklist = None
#       return "stack is deleted"
   
#   def peek(self):
#       if self.isEmpty():
#           return "Stack is empty"
#       else:
#           return self.stacklist[-1]
      
# size = int(input("enter the size of stack :"))
# stackobj = Stack(size)

# while True:
  
#   print("1. push element in stack :")
#   print("2. display stack element :")
#   print("3.check isempty :")
#   print("4.pop operation :")
#   print("5.delete stack :")
#   print("6.peek operation :")
#   print("7. exit")

#   choice = int(input("enter your choice : "))
#   if choice == 1:
#     val = int(input("enter value for stack :"))
#     stackobj.push(val)

#   elif choice == 2:
#     stackobj.displaystack()
  
#   elif choice == 3:
#       print(stackobj.isEmpty())

#   elif choice == 4:
#       print(stackobj.pop())
 
#   elif choice == 5:
#       print(stackobj.deleteStack())

#   elif choice == 6:
#       print(stackobj.peek())
  
#   elif choice == 7:
#       sys.exit()
