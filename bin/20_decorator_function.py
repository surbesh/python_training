"""
Using Decorator Design Pattern
"""

print("Without Using Decorator: We are repeating code in all functions")
print("-"*20)
# -----------------


def add(a, b):
    print("Result is:")
    print(a + b)
    print("End of the result")


def sub(a, b):
    print("Result is:")
    print(a - b)
    print("End of the result")


add(10, 20)
sub(10, 20)


print("#"*40, end="\n\n")
##################################

# Here in add() & sub() function we have few-statements/code are common
# which we need to reuse

print("Our Common Function: WRONG DESIGN: IT WILL NOT WORK")
print("-"*20)
# -----------------

def my_common_func(): # WRONG DESIGN
    print("Result is:")
    print("End of the result")

def add(a, b):
    my_common_func() # WRONG
    print(a + b)
    my_common_func() # WRONG


def sub(a, b):
    my_common_func()
    print(a - b)
    my_common_func()


add(10, 20)
sub(10, 20)

print("THIS IS WRONG DESIGN")

print("#"*40, end="\n\n")
##################################



print("PARTIAL IMPLEMENTATION")
print("Function as per Decorator Design Pattern")
print("for reusing common functionality")
print("-"*20)
# -----------------


# Function as per Decorator Design Pattern
def my_decorator(my_func):
    def decorated_func(x, y): # This can be used for 2 argument functions
        print("Result Is:")
        my_func(x,y)
        print("End Of The Result")
    return decorated_func


# -----------------
# Function-1: add
###################
def my_decorator(my_func):  # my_func = add
    def decorated_func(x, y): # x = 10, y = 20
        print("Result Is:")
        my_func(x,y) # add(10,20)
        print("End Of The Result")
    return decorated_func

def add(a,b):
    print(a + b)

inner_func = my_decorator(add)
# inner_func = decorated_func
# inner_func having reference to decorated_func
inner_func(10, 20)
###################

# -----------------
# Function-2: sub
###################
def my_decorator(my_func): # my_func = sub
    def decorated_func(x, y): # x=10, y=20
        print("Result Is:")
        my_func(x,y) # sub(10,20)
        print("End Of The Result")
    return decorated_func


def sub(a,b):
    print(a - b)

inner_func = my_decorator(sub)
inner_func(10,20)
###################

print("PARTIALLY IMPLEMENTED HERE, Check below block for FINAL DECORATOR")

print("#"*40, end="\n\n")
##################################




print("FINAL and CORRECT IMPLEMENTATION")
print("-"*20)
# -----------------


# Decorator
def my_decorator(my_func):
    def decorated_func(x, y): # This can be used for 2 argument functions
        print("Result Is:")
        my_func(x,y)
        print("End Of The Result")
    return decorated_func


# -----------------
# Function-1: add
###################
@my_decorator
def add(a,b):
    print(a + b)

add(10,20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(add)
# inner_func(10, 20)
###################

# -----------------
# Function-2: sub
###################
@my_decorator
def sub(a,b):
    print(a - b)

sub(10, 20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(sub)
# inner_func(10,20)
###################


print("FINAL and CORRECT IMPLEMENTATION")
print("#"*40, end="\n\n")
##################################


