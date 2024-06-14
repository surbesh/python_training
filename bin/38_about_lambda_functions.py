"""
About Lambda Functions:
- Lambda Functions are functions only but it is not having name
    -- function without name
- It is One Line Function
- Usage:
    -- We can embed inside function argument
    -- We can write lambda function inside list/tuple/set/dictionary
        f = [lambda a, b: a+b, lambda a, b: a-b,]
        f[0](10, 20)
        f[1](10, 20)
"""

print("Add Port Number Function")
print("-"*20)
# --------------

def add_port(ip):
    return ip + ":8080"

ips_list = ["123.123.123.123", "123.123.123.123", "123.123.123.123", "123.123.123.123"]
print("ips_list:", ips_list, end="\n\n")

ips_list_with_port = []
for i in ips_list:
    j = add_port(i)
    ips_list_with_port.append(j)

print("ips_list_with_port:", ips_list_with_port)

print("#"*40, end="\n\n")
##################################

print("Add Port Number Function: Using map() function")
print("-"*20)
# --------------

def add_port(ip):
    return ip + ":8080"

ips_list = ["123.123.123.123", "123.123.123.123", "123.123.123.123", "123.123.123.123"]
print("ips_list:", ips_list, end="\n\n")

ips_list_with_port = map(add_port, ips_list)
# map() function will call add_port() function for each values in ips_list

# ips_list_with_port = []
# for i in ips_list:
#     j = add_port(i)
#     ips_list_with_port.append(j)

print("ips_list_with_port:", list(ips_list_with_port))

print("#"*40, end="\n\n")
##################################

print("Add Port Number Function: Using map() function and Lambda Function")
print("-"*20)
# --------------

# - map is taking function add_port as an argument
# - add_port function we can implemente in one line
#   so, we can write lambda function in map() instead
#   writing separate function add_port()

# def add_port(ip):
#     return ip + ":8080"

# Equellent  lamabda function

# lambda ip : ip + ":8080"


ips_list = ["123.123.123.123", "123.123.123.123", "123.123.123.123", "123.123.123.123"]
print("ips_list:", ips_list, end="\n\n")

ips_list_with_port = map(lambda ip : ip + ":8080", ips_list)

# ips_list_with_port = []
# for i in ips_list:
#     j = add_port(i)
#     ips_list_with_port.append(j)

print("ips_list_with_port:", list(ips_list_with_port))

print("#"*40, end="\n\n")
##################################