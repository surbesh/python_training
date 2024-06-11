"""
MUTABLE
- Dictionary :
    -- We have option to store collection of values like list of names, list of email-ids etc
    -- We can store duplicate values
    -- Here we can provide index to each value. Also called as KEY/VALUE pair
"""

print("Dictionary PART-1")
print("-----------------")

my_dictionary_1 = {0 : "python", 1: 5, 2:"online"}
# Internally it will create object of builtin-class 'dict' and store the values

my_dictionary_2 = dict({0 : "python", 1: 5, 2:"online"})

# FOR KEY: We can Use only IMMUTABLE values for key like numbers, strings, tuple
# FOR VALUES: Values can be any values
my_dictionary_3 = {
    "duration": 5,
    "course": "python",
    "mode": ["Online", "Offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)

print("##################################")



print("Dictionary PART-2")
print("Access each value")
print("-----------------")

my_dictionary = {
    "duration": 5,
    "course": "python",
    "mode": ["Online", "Offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n")

print("Course Name:", my_dictionary["course"]) # "python"
print("2nd character in Course Name:", my_dictionary["course"][1], end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["Online", "Offline"]
print("Last Mode:", my_dictionary["mode"][1]) # "Offline"
print("3rd character in Last Mode:", my_dictionary["mode"][1][2], end="\n\n") # "f"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("Trainer LName:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd char in Trainer LName:", my_dictionary["trainer"]["lname"][1]) # "y"

print("##################################\n")



print("Dictionary PART-3")
print("Methods inside 'dict'")
print("-----------------")

print(dir(dict))

print("##################################\n")


print("Dictionary PART-4")
print("Add/Remove/Update")
print("-----------------")

my_dictionary = {
    "duration": 5,
    "course": "python",
    "mode": ["Online", "Offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

# Add New Element or Update
my_dictionary["location"] = "India"
# If key present then update else add new record

received_value = my_dictionary.pop("duration")
print("received_value from pop():", received_value)

received_value = my_dictionary.popitem()
print("received_value from popitem():", received_value)

print("##################################\n")


print("Extract PICS: 1-WAY")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

start_index = input_data.index("/pics/") # It will return index 1st "/"
start_index = start_index + 6

# 1-way
# end_index = input_data.index("HTTP") # It will return index of H
# end_index = end_index - 1 # Index of space after gif

# 2-way
end_index = input_data.index(" ", start_index)

img = input_data[start_index:end_index]
print(img)

print("###########################")

print("Extract PICS: 2-WAY")
print("--------------")

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

sp= input_data.split()
print("Splitted Values: ", sp, end="\n\n")

raw_img = sp[6] # '/pics/wpaper.gif'

# 1-way: Remove '/pics/' from '/pics/wpaper.gif'
img_1 = raw_img[6:]

# 2-way: Remove '/pics/' from '/pics/wpaper.gif'
raw_img_sp = raw_img.split("/") #
# print(raw_img_sp) # ['', 'pics', 'wpaper.gif']
img_2 = raw_img_sp[2] # Using +ve index no
img_3 = raw_img_sp[-1] # Using -ve index no

print(img_1, img_2, img_3, sep="\n")

print("###########################")

