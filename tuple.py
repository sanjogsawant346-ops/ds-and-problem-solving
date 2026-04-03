#mytuple = ("prashant","ashish","komal","ankush","ashish",77,"sandip",60.52,"prashant")
# print(mytuple)
# print(type(mytuple))
# mytuple[2]="sunil"
# print(mytuple)

# init_tuple =()
# print(init_tuple.__len__())

# init_tuple_a = 'a','b'
# init_tuple_b= ('a','b')
# print(id(init_tuple_a))
# print(id(init_tuple_b))
# print(init_tuple_a == init_tuple_b)

# init_tuple_a ='1','2'
# init_tuple_b = ('3','4')
# print(init_tuple_a + init_tuple_b)
               
# init_tuple = ('python') * 3
# print(type(init_tuple))

# init_tuple = ('python',) * 3
# print(type(init_tuple))

# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1,2),) * 7
# print(len(init_tuple[3:8]))

# names=[4,2,6,2,8,2]
# for i in names:
#     print(i)

# a=[4,0,2,5,0,1]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(i)

# print(a)

# a=[1,2,2,3,4,4,5]
# new=[]
# for i in a:
#      if i not in new:
#           new.append(i)
# print(new)

# l1 = [1,2,3,]
# l2=[2,3,4]
# l3=[3,4,5]
# for i in l1:
#     if i in l2 and i in l3:
#         print(i)


# n=int(input("enter the size of elements in list: "))
# arr=[]
# for i in range(n):
#     val = int(input("enter the element: "))
#     arr.append(val)
# sum =0
# for i in range(n):
#     if i+1 in range(n):
#         sum += abs(arr[i]-arr[i+1])
# print(sum)

# for i in range(1,5):
#   if i==3:
#     break
#   print(i)

# print()
# for i in range(1,5):
#   if i==3:
#     continue
#   print(i)


# for i in range(1,6):
#   if i==3:
#     continue
#   print(i)

# print()
# for i in range(5,0,-1):
#   if i==3:
#     continue
#   print(i)

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3:
#      continue
#     print(i,j)

# name = "sanjog*is*a*good*programmer"
# newname=''
# val=''
# for i in name:
#     if i!='*':
#         newname += i
        
#     else:
#         val +=i
# print(newname)
# print(str(val+newname))

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*c/d)
# print(a+(b*c)/d)

# x=['A,','B','C']
# y=['A,','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)

# a = "listen"
# b = "silent"

# if sorted(a) == sorted(b):
#     print("anagram")
# else:
#     print("not anagram")

#count the words
a ="this is sentence"
count = 1
for i in a:
    if i == " ":
        count += 1
print(count)