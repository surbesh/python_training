"""
Functions: If we want to copy-paste/rewrite same code more than
one time in our program then instead of copy-paste/rewrite
keep that code in a block and we can execute that block
code as many times as we want
"""

print("Without using function")
print("-"*20)
# ---------------

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

a = 10
b = 20
c = a + b
print("Value of c:", c)

print("#"*40, end="\n\n")
####################################

print("Using function")
print("-"*20)
# ---------------

# Function Definition
def my_function():
    a = 10
    b = 20
    c = a + b
    print("Value of c:", c)

# Function Call
my_function()
my_function()
my_function()
my_function()

print("#"*40, end="\n\n")
####################################