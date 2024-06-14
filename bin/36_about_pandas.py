"""
About Pandas
- Pandas is one library
- Pandas has many classes and many functions
- One of the class name is 'DataFrame'
- 'DataFrame' is main class
- 'DataFrame' class has methods related to tabular data
"""

print("DataFrame PART-1")
print("Store Values")
print("-"*20)
# ------------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]])
print(my_df)

print("#"*40, end="\n\n")
###############################

print("DataFrame PART-2")
print("Store Values")
print("-"*20)
# ------------

import pandas as pd
my_df = pd.DataFrame([[10, 20, 30],[40, 50, 60]], index=["r1", "r2"], columns=["c1", "c2", "c3"])
print(my_df)

print("#"*40, end="\n\n")
###############################


print("DataFrame PART-3")
print("Methods inside DataFrame Class")
print("-"*20)
# ------------

print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
###############################


print("Inside Pandas")
print("-"*20)
# ------------

print(dir(pd))

print("#"*40, end="\n\n")
###############################