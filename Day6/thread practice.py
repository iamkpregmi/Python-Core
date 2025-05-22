import threading

def function1():
    for i in range(1, 11):
        print(i)

def function2():
    for i in range(11, 21):
        print(i)


# Create threads
t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

# Start thread execution
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()
