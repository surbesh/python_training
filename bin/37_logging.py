"""
logging library to capture program log
"""

print("Configuring log")
print("-"*20)
# ----------
import logging

my_logging = logging.getLogger()

# Set logging level:
# Example: 'DEBUG' will capture all levels like INFO, DEBUG, CRITICAL, WARNING, ERROR
my_logging.setLevel(logging.DEBUG)
# my_logging.setLevel(logging.ERROR)

# What format we want to print message in file/console
my_log_format = logging.Formatter("%(levelname)s : %(filename)s : %(message)s")

# Configure to print in console
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(my_log_format)
my_logging.addHandler(consoleHandler)

# Configure to write to file
fileHandler = logging.FileHandler("my_log_file.txt", "w")
fileHandler.setFormatter(my_log_format)
my_logging.addHandler(fileHandler)

# From Now we can use my_logging instead of print() function
my_logging.info("This is test Info Message")
my_logging.debug("This is test debug Message")
my_logging.warning("This is test Warning Message")
my_logging.critical("This is test Critical Message")
my_logging.error("This is test Error Message")

print("#"*40, end="\n\n")
##########################

# Below code uses logging instead of print function
##########################
my_logging.info("Testing try/except/finally block")
try:
    my_logging.info("Executing code in try block")
    my_file_handle = open("temp.txt", "w")
    my_logging.info("try block completed")
except Exception as e:
    my_logging.error(f"Got Error in try block, error message is:{e}")
else:
    my_logging.info("Reached else block")
    my_file_handle.write("Hello")
    my_logging.info("else block completed")
finally:
    my_logging.info("Reached finally block")
    my_file_handle.close()
    my_logging.info("File Connection Closed")
##################################


