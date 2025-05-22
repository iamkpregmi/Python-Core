# result = eval(input("Enter inputs: "))
# print(result)

# #command line arguments
# from sys import argv
# sum = 0
# # print(argv)
# for i in argv[1:]:
#     sum += int(i)

# print("Sum of number is:", sum)

# name = "krishnaa"
# print(name.find('i')) #show index of the value, if value not found then throw -1
# print(name.index('u')) #show index of the value, if value not found throw error

# print(name.count('a')) #show number of aqurance

# name = name.replace("krishnaa", "Krishna")
# print(name)

# date = '2025-05-22'

# print(date.split("-"))


# full_name = "Krishna Prasad Regmi"
# print(full_name.split(' '))


# #from the student name list take first and last name
# student_name = ['krishna prasad regmi', 'shubair ali jaidi', 'khalfan khan', 'Brijesh kumar mishra']

# final_output = []
# for student in student_name:
#     fname = student.split(' ')[0]
#     lname = student.split(' ')[-1]
#     result = fname+" "+lname
#     final_output.append(result)


# print(final_output)



# student_list = ['krishna', 'shubair', 'khalfan', 'brijesh']
# result = '-'.join(student_list)
# print(result) # krishna-shubair-khalfan-brijesh



# #First charactor should be Capital
# employee_list = ['krishna', 'Shubair', 'brijesh']

# def to_capital(input):
#     return input.capitalize()


# result = list(map(to_capital, employee_list))
# print(result) #['Krishna', 'Shubair', 'Brijesh']


# # Generators example (Generate fly time value)
# def my_generator():
#     for i in range(5):
#         yield i


# result = my_generator()
# # print(next(result))
# for i in result:
#     print(i)


# # AsyncIO in Python
# import time

# for i in range(10):
#     print(i)
#     time.sleep(2) #wait for 2 seconds


