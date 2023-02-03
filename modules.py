# Modules
# module is basically just you're referencing a file where's libraries is referencing multiple folders and files

import os
import math, datetime, sys

working_directory = os.getcwd()
print(working_directory)


def return_user_id():
    print(os.getpid())


def return_user_name():
    print(os.uname())


print(datetime.date.today())
print(math.remainder(1, 5))
print(sys.path)

