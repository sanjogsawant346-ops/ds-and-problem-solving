# arr = [1, -2, 3, -4, -1, 4]

# pos = [x for x in arr if x >= 0]
# neg = [x for x in arr if x < 0]

# result = []

# for i in range(min(len(pos), len(neg))):
#     result.append(neg[i])
#     result.append(pos[i])

# result.extend(pos[len(neg):])
# result.extend(neg[len(pos):])

# print(result)

mydict = {
    101: "prashant",
    102: "ashish",
    "103":"mohini",
    "104" : "trivani",
    101: "ashish",
    104: "ashish"
}   
# print(mydict)

# a=mydict[102]
# print(a)

# mydict[102] ="peter"
# print(mydict)

# for x in  mydict:
#     print(x)

# for x in  mydict.values():
#     print(x)
# for x ,y in  mydict.items():
#      print(x,y)

# mydict["mobile_no"] =7588341905
# print(mydict)

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])

# a= {'a':1,'b':2,'c':3}
# print(a['a','b'])

# arr = {}
# arr[1] =1
# arr['1'] =2
# arr[1] += 1

# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# my_dist = {}
# my_dist[1] = 1
# my_dist['1'] = 2
# my_dist[1.0] = 4
# sum = 0
# for k in my_dist:
#     sum += my_dist[k]
# print(sum)

# my_dist = {}
# my_dist[(1,2,4)] = 8
# my_dist[(4,2,1)] = 10
# my_dist[(1,2)] = 12
# sum = 0
# for k in my_dist:
#     sum += my_dist[k]
# print(sum)
# print(my_dist)

# box ={}
# jars= {}
# crates={}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# dict ={'c':97, 'a':96, 'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# rec = {"name":"python","age":"20"}
# r =rec.copy()
# print(id(r) == id(rec))
# print(id(r))
# print(id(rec))

# rec = {"name":"Python","age":20,"Addr":"New York"}
# id1 = id(rec)
# del rec
# rec = {"name":"Python","age":20,"Addr":"New York"}
# id2 = id(rec)
# print(id1 == id2) 

# ip= {"x":20,"y":10,"z":30}

# op = min(ip.values())
# print(op)

# ip = {"x":20,"y":10,"z":30}

# op = min(ip, key=ip.get)
# print(op)

# mydict = {101:"sagar",
#           "profession":"developer",
#           "empid":12345,}
# mydict.pop(101)
# print(mydict)

# for i in range (1,4):
#     for j in range(1,4):
#         print(i, end=" ")
#     print() 

# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()


# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i), end=" ")
#     print()

# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):     
#     for j in range(1,n+2-i):     
#         print("*", end=" ")
#     print()

# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):     
#     for j in range(1,n+2-i):     
#         print(chr(64+j), end=" ")
#     print()

# import time
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(2)
#         print(n+1-i, end=" ")
#     print()

# import time
# n = int(input("enter the number of rows: "))
# for i in range (1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()

# def msg(): #called functiom
#     print("hello world..!")

# msg() #calling function
# msg()

# def arithmetic():
#     a = int(input("enter the value of a:"))
#     b = int(input("enter the value of b:"))

#     add = a+b
#     sub =a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# # print(arithmetic())
# result = arithmetic()
# print("Arithmetic=",result)


# def login(username,password):
#     if username == password:
#         print("login succesful")
#     else:
#         print("invalid details")
# username =input("Enter username:")
# password =input("Enter password:")
# login(username,password)

# keyword argument
# def login(username,password):
#     if username == password:
#         print("login succesful")
#     else:
#         print("invalid details")

# login(username="admin",password="admin")

# default argument
# def cityName(city="Goa"):
#     print(city)

# cityName("Delhi")
# cityName("Nagpur")
# cityName()

#variable length argument/variable number of argument
# def nameofCitys(*city):
#     print("City name:",city)

# nameofCitys("Goa","Nagpur","Mumbai","Pune","Nashik")

#wap for menu driven code
# import sys
# def add():
#     v1=int(input("enter value for v1:"))
#     v2=int(input("enter value for v2:"))
#     print("Add:",v1+v2)

# def sub():
#     v1=int(input("enter value for v1:"))
#     v2=int(input("enter value for v2:"))
#     print("Sub:",v1-v2)

# def mul():
#     v1=int(input("enter value for v1:"))
#     v2=int(input("enter value for v2:"))
#     print("Mul:",v1*v2)

# def div():
#     v1=int(input("enter value for v1:"))
#     v2=int(input("enter value for v2:"))
#     print("Div:",v1/v2)

# while True:
#     print("1.Addition")
#     print("2.Substraction")
#     print("3.Multiplication")
#     print("4.Divison")
#     print("5.Exit")

#     choice = int(input("Enter your choice:"))

#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         mul()
#     elif choice == 4:
#         div()
#     elif choice == 5:
#         sys.exit()

programming =  input("Enter your programming name:")
p_name = programming.rstrip()
if p_name == 'Python':
    print(p_name)
elif p_name == 'Java':
    print(p_name)
elif p_name == 'Cpp':
    print(p_name)
else:
    print("Wrong programming name:")