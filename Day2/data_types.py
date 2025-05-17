# myList = ["Krishna","Shubair","Brijesh","Yogendra"]

# # for key,value in enumerate(myList, start=1):
# #     print(key, value)


# marks = [74,85,98,58,74]

# # Zip two list into single unit
# result = zip(myList,marks)
# print(list(result))

# # unzip result into two list
# pairs = [('Krishna', 74), ('Shubair', 85), ('Brijesh', 98), ('Yogendra', 58)]
# list1, list2 = zip(*pairs)
# print(list1)
# print(list2)


# function for the return square of numbers
# def square(num):
#     return num * num


# myList = [1, 2, 3, 4, 5]
# # result = map(square, myList)
# # calculate square using lambda
# result = map(lambda x: x*x, myList)
# print(list(result))


# firstList = [4,6,2]
# secondList = [5,7,3]

# result = map(lambda x,y: x+y, firstList,secondList)
# print(list(result))

# #filter function
# myList = [12,8,7,14,2,3]

# def is_even(num):
#     return num % 2 == 0


# # result = filter(is_even, myList)
# result = filter(lambda x: x%2==0, myList)
# print(list(result))



# # Write a python code for the return word which length more then 5 char
# words = ["apple", "banana", "cherry", "date", "elderberry"]

# result = filter(lambda x: len(x)>5, words)
# print(list(result))

# #Write a python code for filter none value
# values = [0, 1, False, True, [], [1, 2], '', 'hello']
# result = filter(None,values)
# print(list(result))


# from functools import reduce
# myList = [1,2,3,4,5]
# result = reduce(lambda x,y: x*y, myList)
# print(result)


student = {
    'krishna': 500,
    'shubair': 600,
    'brijesh': 300,
    'yogendra':450
}

# fee = student.values()
# from functools import reduce
# result = reduce(lambda x,y: x+y,fee)
# print(result)


# #write a function for the sum of the number
# sum = 0
# for val in fee:
#     sum+= val

# print('Sum is:', sum)

# sum = 0
# for val in student.values():
#     sum += val

# print("Sum is: ", sum)


# myList = [12,85,96,7,86,4]
# searchValue = 7
# try:
#     print(f'Value found in {myList.index(searchValue)} index.')
# except ValueError:
#     print("Value not found in the list.")


