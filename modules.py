# method of logically organizing code for easier use/understanding
# can define functions, classes and variables

# import module - imports module if it is present in a search path
# search path must be specified (a list of directories)

# from can be used to import specific attributes from a module
# from  modname import item1
from fib import fibonacci
# from...import* - imports all items from module

# order of locating modules: current directory -> each directory in shell PYTHONPATH
# -> default path

# namespace is a dictionary of variable names and values
# global variables must be specified
Money = 2000


def AddMoney():
    Money = Money + 1


print Money
AddMoney()
print Money

# ^ will return an error because Money is not global so cannot be called within the function

# setting Money to be global
Money = 2000


def AddMoney():
    global Money
    Money = Money + 1


print Money
AddMoney()
print Money

# dir() function returns a sorted list of strings with names defined in a module
import math
content = dir(math)
print content
# globals() and locals() return names that are global and local namespaces respectively
# locals () called inside a func and returns names that can be accessed locally
# globals() called inside a func and returns names that can be accessed globally
# names can be extracted using keys()
# reload(modname) - reexecutes top-level code in a module (a previously imported mod)

# Package organization (func->mod->file->direc->package)
