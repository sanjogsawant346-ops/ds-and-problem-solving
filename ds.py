# import sys
# class Stack:
  
#   def __init__(self):
#     self.stacklist = [] #stack created

#   def push(self, value):
#     self.stacklist.append(value)
#     print(self.stacklist)

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


# stackobj = Stack()

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

    
#tower of hanoi

# import time
# class tower:
#     def __init__(self):
#         print("welcome to tower of hanoi game")
#         print()
#         print("given problem A=[3,2,1]     B=[]    c[]  ")
#         print()
#         print("expected output")

# class Tower:
#     def tower(self,item):
#         self.A.append(item)
#         time.sleep()
#         print("A:",self.A)
#         print("items in tower A \n")

#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass one completed..............\n")

#     def pass2(self):
#         self.temp = self.A.pop(2)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass two completed..............\n")

#     def pass3(self):
#         self.temp = self.A.pop(0)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass three completed..............\n")

#         import time
# class tower:
#     def __init__(self):
#         print("welcome to tower of hanoi game")
#         print()
#         print("given problem A=[3,2,1]     B=[]    c[]  ")
#         print()
#         print("expected output")

# class Tower:
#     def tower(self,item):
#         self.A.append(item)
#         time.sleep()
#         print("A:",self.A)
#         print("items in tower A \n")

#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass one completed..............\n")

#     def pass2(self):
#         self.temp = self.A.pop(2)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass two completed..............\n")

#     def pass3(self):
#         self.temp = self.A.pop(2)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass two completed..............\n")
#         import time
# class tower:
#     def __init__(self):
#         print("welcome to tower of hanoi game")
#         print()
#         print("given problem A=[3,2,1]     B=[]    c[]  ")
#         print()
#         print("expected output :")


# class Tower:
#     def tower(self,item):
#         self.A.append(item)
#         time.sleep()
#         print("A:",self.A)
#         print("items in tower A \n")

#     def pass1(self):
#         self.temp = self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass one completed..............\n")

#     def pass2(self):
#         self.temp = self.A.pop(2)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass two completed..............\n")

#     def pass3(self):
#         self.temp = self.A.pop(2)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass three completed..............\n")

#     def pass4(self):
#         self.temp = self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass four completed..............\n")

#     def pass5(self):
#         self.temp = self.A.pop(1)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A :",self.A   ,"  ","B :",self.B  ,"  ","C :",self.C)
#         print("Pass two completed..............\n")
