# math = 50
# name = "prashant" 
# pi = 3.14
# result = True 

# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))

# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result))

# math = 50 #new memory
# chem = 50
# hindi = 60
# print(id(math))
# print(id(chem))
# print(id(hindi))

# print(2+2)
# print("2"+"2")

# val1 =int(input("enter value of val 1:"))#2
# val2 =int(input("enter value of val 2:"))#4
# print (val1 + val2)

# int() used to convert in integer
# print(int(3.14))
# print(int(10+5j))
# print(int(True)) #=1
# print(int(False)) #=0
# print(int("4.22")) 
# print (int("4"))
# print(int("Prashant")) 

# we cannot convert  complex value to int
# we cannot convert  floating value strig  to int
# can't convert string name to int

# #float() used to convert 
# print(float(3)) #3.0
# #print(float(50+2j))
# print(float(True)) #1.0 
# print(float(False)) #0.0 
# print(float(4.22))
# print(float("4"))
# #print(float("name"))

# we cannot convert  complex value to float
# can't convert string name to float

# complex() is used to convert
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# #print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))

# # bool() is used to convert
# print(bool(0)) #false
# print(bool(15)) #True
# print(bool(3.14)) #True
# print(bool(0.0)) #False
# print(bool(1+2j)) #True
# print(bool(0+0j)) #False
# print(bool(-1)) #True
# print(bool(False)) #False
# print(bool(True)) #true
# print(bool()) #false
# #print(bool("prashant")) #true

#there are 33 reserve keywords in python

#swapping program
# val1 =int(input("enter value for val1:"))
# val2 =int(input("enter value for val2:"))

# print("before swapping val1:",val1)
# print("before swapping val2:",val2)

# temp = val1
# val1 = val2
# val2 = temp

# print("after swapping val1:",val1)
# print("after swapping val2:",val2)

# a=int(input("enter value for val1:"))
# b=int(input("enter value for val2:"))

# print("before swapping val1:",a)
# print("before swapping val2:",b)

# a=a+b
# b=a-b
# a=a-b

# print("after swapping val1:",a)
# print("after swapping val2:",b)

# marks of 3 subjects

# p1 = int(input("enter marks of p1:"))
# p2 = int(input("enter marks of p2:"))
# p3 = int(input("enter marks of p3:"))
            
# total = p1+p2+p3
# percentage = total/3.0
# print("Total =", total)
# print("percentage =", percentage)

#simple interest

# p_amount = int(input("enter principal amount:"))
# roi = int(input("enter rate of interest:"))
# time = int(input("enter the duration of loan amount:"))

# si = p_amount * roi * time/100
# print("simple intrest=",si)

# wap to enter user height in feet and convert into inch and centimeter

# height = float(input("enter the height in feet:"))

# inch = height * 12
# cm = inch * 2.54

# print("height in inch:",inch)
# print("height in cm:",cm)

#reverse the number

# num = 123 #321
# a = num % 10 # a=3
# num = num // 10 #num=12
# b = num % 10 #b=2
# c = num // 10 #c=1
# rev = a*100+b*10+c
# print(rev)

#num = 123456

# identity operator
# a = 10
# b = 10
# print( a is b)#true
# print(a is not b)#false


# a = 15
# b = 10
# print( a is b) #false
# print(a is not b) #true

# membership operator

# name =  "help4code"
# print("z" in name) #false
# print("p" in name) #true


#wap to accept any one no  and check pos,neg and zero
#no = int(input("enter any one number:"))
# if no > 0:
#     print("positive number")
# if no < 0:
#     print("negative number")
# if no == 0:
#      print("number is 0")

#enter 5 no and find maximum no

# a = int(input("enter 1st no"))
# b = int(input("enter 2nd no"))
# c = int(input("enter 3rd no"))
# d = int(input("enter 4th no"))
# e = int(input("enter 5th no"))

# if a>b and a>c and a>e and a>d:
#     print(a," is greater")
# if b>a and b>c and b>d and b>e:
#     print(b," is greater")
# if c>b and c>a and c>e and c>d:
#     print(c," is greater")
# if d>b and d>c and d>e and d>a:
#     print(d," is greater")
# if e>b and e>c and e>a and e>d:
#     print(e," is greater")

#log in code

# username  = input("enter username:")
# password  = input("enter password:")
# if username == password:
#     print("login succesful")
# else:
#     print("invalid credentials")

#Wap to accept phy chem and maths subjects calculate total and  percentage and percentage is greater than equal to 60 and gender is equal to male so he is eligible for the placement else eligible for data entry job
# phy = int(input("enter marks of physics:"))
# chem = int(input("enter marks of chemistry:"))
# maths = int(input("enter marks of maths:"))
# gender = input("enter the gender(male/female):")

# total = phy+chem+maths
# percentage =total/3

# if percentage>=60 and gender == "male":
#     print("eligible for placement")
# else:
#     print("eligible for data entry job")


#nested if else wap to accept value of  A,B,C and find max value
# p1 = int(input("enter any no:"))
# p2 = int(input("enter any no:"))
# p3 = int(input("enter any no:"))

# if p1 > p2:
#     if p1 >p3:
#         print(p1,"is greater")
#     else:
#         print(p3,"is greater")
# else:
#     if p2> p3:
#        print(p2,"is greater")
#     else:
#         print(p3,"is greater")



# day = input("enter your day name :")

# if day == "saturday" or day=="SATURDAY" or day == "sunday" or day == "SUNDAY":
#     print("weekend")
# else:
#     print("working day")


# char = ord(input("enter any char:"))
# if char >=65 and char<=91:
#      print("it is a character is in uppercase")
# elif char>=97 and char<=122:
#      print("it is a character is in lowercase")
# elif char>=48 and char<=57:
#      print("it is a number")
# else:
#     print("it is a special character")

# Amount = int(input("please enter amount for withdraw:"))
# print(" 100 notes=",Amount//100)
# print(" 50 notes=",(Amount%100)//50)
# print(" 20 notes=",((Amount%100)%50)//20)
# print(" 10 notes=",(((Amount%100)%50)%20)//10)
# print(" 5 notes=",((((Amount%100)%50)%20)%10)//5)

