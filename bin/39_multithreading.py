"""
multithreading:
- One Process can be splitted into smaller pieces and run parallelly
- each piece is called thread

In python multithreading is NOT PARALLEL
- Internally there is a LOCK called GLOBAL INTERPRETER LOCK
    - It will make sure to execute one code at a time

Why we need to use multithreading in python if it is not parallel?
- Answer: if some thread is waiting for some resources then that
    waiting time, we can make use execute other threads

If we want pure parallel execution then we can make use of multiprocessig
"""
print("Without using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


input_list = [10, 20, 30, 40]
square_function(input_list)
cube_function(input_list)

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#####################################

print("Using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


input_list = [10, 20, 30, 40]

from threading import Thread

square_thread = Thread(target=square_function, args=(input_list, ))
cube_thread = Thread(target=cube_function, args=(input_list, ))

# Start the thread
square_thread.start() # It will not wait for square_function() to complete
# Instead it will just call square_function() and procced to next line
cube_thread.start()# It will not wait for cube_function() to complete
# Instead it will just call cube_function() and procced to next line

# using join(), We are making threads to wait till it completes
square_thread.join()
cube_thread.join()

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#####################################

print("WITH DELAY: Without using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


input_list = [10, 20, 30, 40]
square_function(input_list)
cube_function(input_list)

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#####################################

print("WITH DELAY: Using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


input_list = [10, 20, 30, 40]

from threading import Thread

square_thread = Thread(target=square_function, args=(input_list, ))
cube_thread = Thread(target=cube_function, args=(input_list, ))

# Start the thread
square_thread.start() # It will not wait for square_function() to complete
# Instead it will just call square_function() and procced to next line
cube_thread.start()# It will not wait for cube_function() to complete
# Instead it will just call cube_function() and procced to next line

# using join(), We are making threads to wait till it completes
square_thread.join()
cube_thread.join()

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#####################################






