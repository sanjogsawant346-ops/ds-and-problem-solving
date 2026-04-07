# print('prasahantjha777'.isalnum())
# print('prashantjha'.isalpha())
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Prashant '.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

# print("Prashant".find("z"))
# print("Prashant".index("r"))
# print("Prashant jha".count("a"))

# dict ={"name":"Alice","age":30} 
# if "age" in dict:
#     print("age key is exists")

#code to count frequency of each element in a list 
# my_list = [1,2,2,3,4,3,5]
# frequency_dict = {}
# for item in my_list:
#     if item in frequency_dict:
#         frequency_dict[item] += 1
#     else:
#         frequency_dict[item] = 1
# print(frequency_dict)


# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# try:
#     result = n1 / n2
#     print("The result of division is:", result)
# except:
#     print("Division by zero is not allowed.")


# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     result = n1 / n2
#     print("The result of division is:", result)
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# except ValueError:
#     print("Invalid input. Please enter numeric values.")


# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     result = n1 / n2
    
# except(ZeroDivisionError, ValueError) as e:
#     print("An error occurred:", e)

# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     result = n1 / n2
    
# except(ZeroDivisionError, ValueError) as e:
#     print("Enter correct no:", e)
# except:
#     print("this is default except block")

# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     result = n1 / n2
    
# except(ZeroDivisionError, ValueError) as e:
#     print("Enter correct no:", e)
# else:
#     print("everything is ok")


# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     result = n1 / n2
    
# except(ZeroDivisionError, ValueError) as e:
#     print("Enter correct no:", e)
# finally:
#     print(" i will always execute")

# #nested try except block
# try:
#     n1 = int(input("Enter the first number: "))
#     n2 = int(input("Enter the second number: "))
#     try:
#         result = n1 / n2
#         print("The result of division is:", result)
#     except ZeroDivisionError as e:
#         print(e)
# except ValueError as e:
#     print(e)

# try:
#     a=int(input("enter first integer no :"))
#     b=int(input("enter second integer no:"))
#     print(a/b)
# except (ValueError,ZeroDivisionError) as message :
#     print(message)
# else:
#     print("there is no error in try block")
# finally:
#     print("I am finally block i akways whether exception")

# data = [5,7,8,3,7,8,9,2,3]
# n = 0
# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         if data[i] == data[j]:
#             n += 1
# print(n)   

# mylist = [5,7,8,3,7,8,9,2,3]
# newlist = []

# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]

#     j=i+1
#     while j<len(mylist):
#         if key == mylist[j]:
#             newlist.append(key)
#         j = j+1
# print(len(newlist))

# list = [7,3,9,2,8]
# list.sort()
# print(list)
# print(list[-2])

# i=1
# while i<=5:
#     print(i)
#     i= i+1

# username =""
# password =""
# while username !="admin" or password !="admin":
#     username = input("Enter username:")
#     password = input("Enter password:")

    
# name ='programming'
# vowels =['a','e','i','o','u']
# cons = 0
# vowel = 0
# for i in name:
#     if i in vowels:
#         vowel += 1
#     else:
#         cons += 1

# print("consonents:",cons)
# print("vowels:",vowel)


# def remove_occurrences(lst, element):
#     return [item for item in lst if item != element]
# my_list = [1, 2, 2, 3, 4, 2]
# element_to_remove = 2

# result = remove_occurrences(my_list, element_to_remove)
# print(result)

# list = [2,3,4,5]
# product = 1
# for i in list:
#     product = product*i
# print(product)

# f = open("myfile.txt","w")
# print("name of file:",f.name)
# print("file mode   :",f.mode)
# print("readable: ", f.readable())
# print("writable: ", f.writable())
# print("file.closed: ", f.closed)
# f.close()
# print("file.closed: ", f.closed)

# f = open("myfile.txt", "a")
# f.write("\n sawantwadi is smart city")
# f.close()
# print("file opration is done")

# f = open("myfile.txt", "w")
# mylist =["prashant","mahesh","suresh"]
# mytuple =("prashant","mahesh","suresh")

# f.writelines(mylist)
# f.writelines(mytuple)

# f.close()
# print("written work has done succesfully")
# print("file opration is done")

# f = open("myfile.txt","r")
# print(f.read())
# f.close()

# with open("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("prashant\n")
#     print("file closed:",f.closed)
# print("file closed:",f.closed)

# with open("myfile.txt","r") as f:
#     content = f.read()
#     print(content)


# f1 = open ("134080861660368200.jpg","rb")
# f2 = open ("demo.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("new image is available with name:")

# import csv
# f = open ("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["studentID","rollno","name","mobileno"])

# studentid= int(input("Enter student id:"))
# rollno = int(input("Enter your roll no:"))
# name= input("enter your name:")
# mobileno= int(input("Enter your mobile no:"))
# a.writerow([studentid,rollno,name,mobileno])
# print("student records has saved")

# import csv
# f = open ("newfile.csv","a",newline="")
# a = csv.writer(f)
# a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])

# rollno = int(input("Enter your roll no:"))
# name= input("enter your name:")
# mobileno= int(input("Enter your mobile no:"))
# p1 = int(input("enter value of p1:"))
# p2 = int(input("enter value of p2:"))
# p3 = int(input("enter value of p3:"))

# email = input("enter email:")
# total = p1+p2+p3
# percentage = total /3
# a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"])
# print("student records has saved")

import csv
f = open("student.csv", "a", newline = "")
a = csv.writer(f)
a.writerow(["studentID","rollno","name","mobileno","email","marks1","marks2","marks3","total","percentage","result"])
studentid = int(input("enter the studentID:"))
rollno = int(input("enter the rollno:"))
name = input("enter the name:")
mobileno = int(input("enter the mobileno:"))
email = input("enter the email:")
marks1 = int(input("enter the marks1:"))
marks2 = int(input("enter the marks2:"))
marks3 = int(input("enter the marks3:"))
percentage = (marks1+marks2+marks3)/3
if percentage >= 40:
    result = "pass"
else:
    result = "fail"
    
a.writerow([studentid,rollno,name,mobileno,email,marks1,marks2,marks3,marks1+marks2+marks3,percentage,result])
print("student record has save")
