# Reading data form the file
# file = open('firstfile.txt',"r")
# content = file.read()
# print(content)
# file.seek(0) # Reset file pointer to the beginning
# lines = file.readlines() # Reads all lines into a list
# print(lines)
# for text in lines:
#     print(text,end="")
# line = file.readline() # Reads one line at a time
# print(line)

# # Writing operation on the python
# file = open("filename.txt", "w")
# # file.write('hello world\nthis is the second line')
# file.writelines(["line1\n", "line2\n"]) # Writes a list of strings to the file

# file = open("filename.txt", "a")
# file.write("This is appended text.\n")

# file.close() #close the file


# # file operation using with operator
# with open("firstfile.txt","r") as file:
#     content = file.read()
#     print(content)


# try:
#     file = open("firstfile.txt","r")
#     content = file.read()
# except:
#     file = open("firstfile.txt","w")
#     file.write("Hello World!")
#     file.close()
#     print("File created successfully")
# else:
#     print(content)
