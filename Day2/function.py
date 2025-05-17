# A function in Python is a block of organized, reusable code that performs a specific task. 
# Functions help to break down larger programs into smaller, more manageable parts, 
# making code easier to read, understand, and maintain. There are built-in functions that are 
# provided as part of the Python language and user-defined functions which are defined by the programmer. 


# basic function (default return null)
def wish():
    print('hello world')


# function takes one areuments with return
def wish(name):
    return "Hello " + name


# function with default argument
def wish(name='user'):
    return "Hello "+name

# function that takes two arguments with default argument
def sum(first=0,second=0):
    return first + second


# *args (Non-keyword Arguments) set type
def sum_args(*args):
    sum = 0
    for arg in args:
        sum += arg

    return sum


my_list = [1,2,3,4,5]
# sum_args(my_list)

# print(sum_args(1,2,3,4,5))
# print(sum_args(my_list))


# **kwargs (Keyword Arguments) dict type
def show_kwargs(**kwargs):
    print(kwargs)


# print(show_kwargs(name='krishna',age=25))

my_dict = {
    "name": "Krishna",
    "age": 25,
    "city": "Delhi"
}

# show_kwargs(name=my_dict)

#combine *args and **kwargs
def combine_value(*args, **kwargs):
    print(args)
    print(kwargs)


# combine_value(41,78,name="krishna", age=25, city='delhi')

# Print kay value pair data from the dict
# for key,value in my_dict.items():
#     print(key, value)


# ----------------------------------------------------------------
# lembda function / Anonymus function

# product = lambda a,b: a*b
# print(product(4,6))


# lembda function with default arguments
# product = lambda a=1,b=1: a*b
# print(product())
# print(product(4,3))




def get_name_and_age():
    return "krishna",25


# name, age = get_name_and_age()
# print(name, age)
# print(get_name_and_age())

