# Packages and Libraries 


when building a program, it is really important to think whether to build a class/object or to use a function. you may not even need to make a function yourself if there is a module that does what you are looking for already. 

### Built-in functions
- Print()
- len()
- type()

### Libraries
A library is a set of RELATED modules or packages bundled together.
```python
from random import random
import math
# print(random.random())
print(random())

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
```
this code uses the python libraries random to print a random number. also it uses the math libraries so that you can use modules to change the float 23.66
### Modules 

A module is a collection of code or functions that uses the .py extension - allowing you to use that code/functions in your program

```python
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
```
This code block uses modules to print out the date, what system path you are using and uses the math module to find the reminder of 1 and 5. 

### packages 

A Python package usually consists of several modules. Physically, a package is a folder containing modules
![](structure-of-packages.webp)
