"""
Get data from server_log.txt
then
extract using regular expression
then
send extracted info to database
"""

"""
How to communicate with databases in python?

python-program  <--Communicate Using Library-->  Any Databases(SQL/No-SQL)

Example:
python-program  <--Communicate Using Library (cx-oracle)-->  Oracle Databases
python-program  <--Communicate Using Library (mysql-connector-python)-->  MySQl Databases
python-program  <--Communicate Using Library (sqlite3)-->  SQLite Databases
"""

"""
We need database.
- We can use SQLite database

How to create/communicate SQLite database?
OPTION-1: Install SQLite Database Software
OPTION-2: Without Installing SQLite Database Software, 
        Using python library 'sqlite3', We can create/communicate SQLite database. 
"""

print("Create database and table")
print("-"*20)
# ----------------

import sqlite3

print("Create/Connecting to database 'my_database.sqlite3' ")
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("Done\n")

print("Creating cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Creating table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")


print("#"*40, end="\n\n")
#########################################


print("Read data from server_log.txt")
print("-"*20)
# ----------------

# Step-1: Connect to file
# ----------------
my_log_file_handle = open(r"../log/server_log.txt", "r")

# Step-2: Read
# ----------------
file_content_in_list = my_log_file_handle.readlines()
print(file_content_in_list)

# Step-3: Disconnect
# ----------------
my_log_file_handle.close()

print("#"*40, end="\n\n")
#########################################

print("Extract Info and write to database")
print("-"*20)
# ----------------

import re

for each_line in file_content_in_list:
    match_result = re.match('(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*?(GET|POST|PUT|PATCH|DELETE)\s+/(pics/(\w+\.(gif|jpg)))?.*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        img = match_result.group(5)
        if img is None:
            img = "No Image"
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}','{dt}','{img}')"
        # f -> format
        # f -> replaces {var_name} with variable value
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One Record Inserted\n")

my_db_connection.commit()
print("All Records are inserted\n")

my_db_connection.close()
print("DB Connection Closed\n")

print("#"*40, end="\n\n")
#########################################




