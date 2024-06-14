"""
Get data from db and produce below reports
db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
db_dump_6.html
"""


print("Get data from database")
print("-"*20)
# ----------------
import pandas as pd
import sqlite3
my_db_connection = sqlite3.connect("my_database.sqlite3")
my_query = "SELECT * FROM MY_TABLE"
my_db_df = pd.read_sql(my_query, my_db_connection)
print(my_db_df)

print("#"*40, end="\n\n")
#########################################

print("Write to file")
print("-"*20)
# ----------------

# db_dump_1.txt
my_db_df.to_csv("db_dump_1.txt", sep="\t") # default sep=","

# db_dump_2.csv
my_db_df.to_csv("db_dump_2.csv")

# db_dump_3.xlsx
my_db_df.to_excel("db_dump_3.xlsx", sheet_name="My_DB_DATA")

# db_dump_4.json
my_db_df.to_json("db_dump_4.json")

# db_dump_5.xml
my_db_df.to_xml("db_dump_5.xml")

# db_dump_6.html
my_db_df.to_html("db_dump_6.html")

print("""Created Below Files
db_dump_1.txt
db_dump_2.csv
db_dump_3.xlsx
db_dump_4.json
db_dump_5.xml
db_dump_6.html

Please check
""")

print("#"*40, end="\n\n")
#########################################