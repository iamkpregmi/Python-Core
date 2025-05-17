# name = input("Enter name: ")
# age = int(input("Enter your age: "))
# print(f"Hello {name} is a good person, your age is {age} years.")


# #write a python program that convert negative number to positive number
# age = int(input("Enter your age: "))
# age = (age*-1) #logic for the convert negative number to positive number using bitwise operator
# print("Your age is", age)


# mydata = 5+9j
# # print(mydata, type(mydata))
# print(mydata)

# name = 'krishna'
# print(name, type(name))

# #Range function(0 to n-1)
# # print 2 to 20 (even number)
# for i in range(2,20+1, 2):
#     print(i,end=" ")

# # print number in reverse order
# for i in range(10,0,-1):
#     print(i, end=" ")

# # Reverse a list
# myList = [74,96,87,41,8]
# for item in range(len(myList)-1,-1,-1):
#     print(myList[item],end=" ")

# a = 91
# b = 10
# x = 78
# y = 91
# # print(not(a>b or x<y))
# # print(a is y) #both variable refer same object

# print(a is not b)

# myList = [74,85,89,7,85,741,5,8]
# skip_value = int(input("Enter a number you want to skip: "))
# for i in myList:
#     if skip_value == i:
#         continue
#     print(i)

# find_value = int(input("Enter number you want to find: "))
# index = 0
# for i in myList:
#     if find_value == i:
#         print(f'{find_value} found in {index} index')
#         break
#     index += 1
#     if(index >=len(myList)):
#         print("Value not found in the list")

# newList = []
# num = 85
# for i in myList:
#     if num!=i:
#         newList.append(i)

# print(myList)
# print(newList)

# unique_list = []
# for i in myList:
#     if i not in unique_list:
#         unique_list.append(i)

# print(unique_list)

    
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.update({'color': 'White'}) #insert new key value into dict
# print(car) #print dict

# print(car.keys(), car.values()) #print all keys and values of the dict

# for i in car:
#     print(i, car[i]) #print all dict data key value pair

# #Replace dict value
# car["brand"] = "Tesla" #if key found then replace value otherwise create new one
# print(car)

# car.update({'new_brand': car['brand']})
# del car['brand']
# print(car)


# # Write a python program for the frequency count
# myList = [74,85,89,7,85,741,5,8]
# frqu_count = {}
# for i in myList:
#     if i in frqu_count:
#         frqu_count[i] += 1
#     else:
#         frqu_count[i] = 1

# print(frqu_count)

# from collections import Counter
# myList = [74, 85, 89, 7, 85, 741, 5, 8]
# frqu_count = Counter(myList)
# print(frqu_count)



# #list comphersion
# myList = [5,2,3,7,9,12,1]
# new_list = [i for i in myList if i%2==0]
# print(new_list)

