# data=int(input("Enter the number"))
# if(data < 0):
#     print("Number is -ve number")
# elif(data == 0):
#     print("Number is Zero")
# else:
#     if(data % 2 == 0):
#         print("It is a even Number")
#     else:
#         print("It is a Odd Number")
# a="madam"
# b=""
# l=len(a)
# print(l)
# for i in range((l-1),-1 , -1):
#    b=b+a[i]
# print(b)
# if(a == b):
#     print("palendrom")
# else:
#     print("not a palendrom")


# a="satyaaatprakash"
# b=""
# for i in a:
#     if i not in b:
#         b=b+i
# print(b)


# print("Satya".istitle())
# print("satya".istitle())
#
# a="satya"
# b="bhubaneswar"
# print(f'My name is {a} and I am from {b}')

# Python3 code to demonstrate working of
# Convert numeric words to numbers
# Using word2number
# Python3 code to demonstrate working of
# Avoid Last occurrence of delimiter
# Using map() + join() + str()

# initializing list
# test_list = [4, 7, 8, 3, 2, 1, 9]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # initializing delim
# delim = "$"
#
# # map extends string conversion logic
# res = delim.join(map(str, test_list))
#
# # printing result
# print("The joined string : " + str(res))


# a= "satya prakash"
# len= sum(map(len , a.split()))
# print(len)
#
# a="I am Satya Prakash"
# b=len(a.replace(" " , ""))
# print(b)
# res=len(b)
# print(str(res))


a="this is a python Program"
a=a.split(" ")
for i in a :
    if len(i) % 2 == 0:
        print(i)