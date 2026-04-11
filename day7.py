# #sort dictionary by key or value
# ip= {"A":1,"B":2,"C":3}
# #op ={c,b,a}
# desc = dict(sorted(ip.items(),reverse=True))
# asc = dict(sorted(ip.items()))
# print(asc)
# print(desc)

# # #remove all element from dict
# ip = {"A":1,"B":2,"C":3}
# a = ip.clear()
# print(ip)

# def findBiggestNumber(array):
#     firstValue = array[0] #---------------------O(1)
#     for i in range(1,len(array)): #----------------------|O(n)|----O(n)
#         if array[i] > firstValue: #-------------O(1)|----|O(1)|
#             firstValue = array[i] #-------------O(1)|
#     return firstValue


# array = [2,4,5,6,7,1,9,3,4,5,6]
# print(findBiggestNumber(array))#-------------------O(1)
# #time complexity : O(1)+O(n)+O(1) = O(N)

# #write a program to print the number of special characters in a string
# def countSpecialCharacters(string):
#     special_characters = "!@#$%^&*()_+-=~`|\\:;\"'<>,.?/"
#     count = 0
#     for char in string:
#         if char in special_characters:
#             count += 1
#     return count

# string = "Hello, World! How are you??"
# print(countSpecialCharacters(string))


# import math

# size = int(input("Enter the number of elements: "))
# a = []

# for i in range(size):
#     element = int(input(f"Enter element {i+1}: "))
#     a.append(element)

# count = 0
# for i in a:
#     if math.sqrt(i).is_integer():
#         count += 1

# print(" square roots count:", count)


# def linearsearch(array, target): #[1,2,3,4,5,6,7,8]
#     for i in range(len(array)):#i=2 ----------------------------------------->O(n)
#         if array[i] == target:# == 4 ---------------------------------------->O(1)
#             return i #------------------------------------------------------->O(1)
#     return -1 #-------------------------------------------------------------->O(1)

# array = [1,2,3,4,5,6,7,8]
# target = 4 # int
# result = linearsearch(array,target)
# if result == -1:
#     print("Element not found")
# else:
#     print("Element found at index",result)


# def binarySearch(array,target): 
#     start = 0
#     end = len(array)-1
#     while start <= end:
#         mid = (start+end) //2
#         if array[mid] == target:
#             return mid
#         elif array[mid]< target:
#             start = mid+1
#         else:
#             end = mid -1
#     return -1 
    
# sorted_array =[1,2,3,4,5,6,7,8,9]
# target = 5
# result=binarySearch(sorted_array, target)
# if result == -1:
#     print("not found")
# else:
#     print('Element found at index no=',result)