# #simple exception handeling
a = 10
b = 2
# try:
#     result = a / b
#     print('Result', result)
# except:
#     print('Something Wint Wrong')


# try:
#     result = a / b #check exception
# except ZeroDivisionError as e:
#     print(f"Error: {e}") #if exeption found show error
# else:
#     print('Result is', result) #execute this block if no error found
# finally:
#     print('Function work successfully') #always run this block


# # Custom Error
# def is_positive(num):
#     if num < 0:
#         raise ValueError('Number should be Positive')  
#     # print(f"Age: {num}")
    
# age = -18

# try:
#     is_positive(age)
# except ValueError as e:
#     print(f'Error: {e}')
# else:
#     print('Age:',age)


# # Raise New Custom Error
# class CustomError(Exception): #need to inherit exception Class
#     pass

# def is_positive(age):
#     if age < 0:
#         raise CustomError('Number Should be Positive new')
    
# age = -15
# try:
#     is_positive(age)
# except CustomError as e:
#     print(f'Error: {e}')
# else:
#     print('Age', age)


# #class in python
# class Human:
#     def __init__(self):
#         print('this is the constructor')

#     def msg(self, user='user'):
#         print(f"Hello: {user}")


# myObj = Human() #object of the class
# myObj.msg("Krishna")





