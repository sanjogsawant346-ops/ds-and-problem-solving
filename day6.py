# #wap to reverse  each word in string
# str = "hello world"
# list = str.split()
# new_list = []
# for item in list:
#     new_list.append(item[::-1])
# print(" ".join(new_list))


# # #wap to compress  abstring by replacing consecutive characters with their count
# string = "aaabbbccc"
# newstring = ""
# count = 1
# for i in range(len(string)-1):
#     if string[i] == string[i+1]:
#         count = count + 1
#     else:
#         newstring = newstring + str(count) + string[i]
#         count = 1
# newstring = string[len(string)-1] +  newstring + str(count) 
# print(newstring)

# from abc import ABC, abstractmethod
# class help4code(ABC):
#     @abstractmethod #decorator
#     def training(self):
#         pass

#     @abstractmethod
#     def placement(self):
#         pass
# class Ashish(help4code):
#     def training(self):
#         print("c, c++, java")
#     def placement(self):
#         print("java placement")
# class Ankush(help4code):
#     def training(self):
#         print("python | django")
#     def placement(self):
#         print("python placement")
# class Prashant(help4code):
#     def training(self):
#         print("machine learning")
#     def placement(self):
#         print("Data science placement")
# obj1 = Ashish()
# obj2 = Ankush()
# obj3 = Prashant()
# obj1.training()
# obj1.placement()
# obj2.training()
# obj2.placement()
# obj3.training()
# obj3.placement()

# from abc import ABC,abstractmethod
# class Irctc(ABC):
#     @abstractmethod
#     def bookTicket(self):
#         pass
# class MakeMyTrip(Irctc):

#     def bookTicket(self):
#         print(" ===============================================")
#         print("Welcome to makemytrip.com")
#         source = input("enter a source station name:")
#         destination = input("enter a destination station name:")
#         date = input("enter date:")
#         print(" ================================================")
# class GoIbbibo(Irctc):

#     def bookTicket(self):
#         print(" ===============================================")
#         print("Welcome to goibibo.com")
#         source = input("enter a source station name:")
#         destination = input("enter a destination station name:")
#         date = input("enter date:")
#         print(" ================================================")

# class Yatra(Irctc):

#     def bookTicket(self):
#         print(" ===============================================")
#         print("Welcome to Yatra.com")
#         source = input("enter a source station name:")
#         destination = input("enter a destination station name:")
#         date = input("enter date:")
#         print(" ================================================")

# obj1=MakeMyTrip()
# obj1.bookTicket()
# obj2=GoIbbibo()
# obj2.bookTicket()
# obj3=Yatra()
# obj3.bookTicket()

# class Base:
#      def __init__(self):
#           print("Parent class constructor called")
#           self.a = "prashant" #public
#           self.__c = "Ashish" #private
# class Derived(Base):
#      def __init__(self):
#           Base.__init__(self)
        #   print(self.a)
        #   print(self.__c)
# obj = Derived()
# print(obj.a) #accesible
# print(obj.__c)#not accesible

# obj1 = Base()
# print(obj1.a) #accesible
# print(obj1.__c) #not 

# class Rbi:
#     #delcaring public method
#     def publicPolicy(self):
#         print("check public poliocy of Rbi")

#     #declaring private method
#     def __privatepolicy(self):
#         print("there is some private policy which is not accesible for public")

# class Sbi(Rbi):
#     def __init__(self): #first sbi class const called
#         Rbi.__init__(self) #second parent class constr called
    
#     def callingPublicMethod(self): #childclass public method
#         self.publicPolicy() #calling parentclass public method

#     def callingPrivateMethod(self): #childclass public method
#         self.privatePolicy() #calling parentclass private method

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()   
# obj1.publicPolicy()
# obj1.__privatepolicy()
# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatepolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2._Rbi__privatepolicy()

# ip = [10,98,3,33,12,22,21,11]
# even =[]
# odd = []
# for i in ip:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even+odd)

