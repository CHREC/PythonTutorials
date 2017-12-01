#  block of code that performs an action that can be reused
def()  # function blocks starts by defining the function
#  input params/args placed w/in parenthesis--parameters can also be defined
# parameters in parenthesis is followed by a colon
# return[expression] exits a function -- no expression = returns nothing


def funcname(params, args):
    "function_docstring"
    function_suite
    return[expression]

# example 1 of function


def printme(str):
    "This prints a passed string into this function"
    print str
    return


# calling the example function 1
printme("Printed by calling the user defined function")

# example 2 of function


def changeme(myList):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4])  # .append overwrites argument passed by reference
    print "Values inside the function: ", myList
    return


# calling the example function 2
mylist = [10, 20, 30]
changeme(mylist)
print "Value outside the function: ", mylist

# example 3 of function


def changeme(mylist):
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4]  # will assign new reference in mylist [does not affect
    # mylist outside of the function]
    print "Values inside the function: ", mylist
    return


# calling the example function 3
mylist = [10, 20, 30]
changeme(mylist)
print "Values outside the function: ", mylist

# Arguments can be required, a keyword, defaulted, or of variable-length
# Required args - the number of args and the order must match when calling


def printme(str):
    "This prints a passed string into this function"
    print str
    return


printme()  # -> will result in an error

# Keyword args - in function calls, the args are identified by parameter name
# can be skipped or placed out of order


def printinfo(name, age):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age ", age
    return


printinfo(age=21, name="sid")

# Default args - assumes a default valye if one is not provided when function is called


def printinfo(name, age=35):
    "This prints a passed info into this function"
    print "Name: ", name
    print "Age ", age
    return


printinfo(age=21, name="sid")
printinfo(name="sid")

# Variable-length args - dunction might need to process multiple args sometimes


def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print "Output is: "
    print arg1
    for var in vartuple:
        print var
    return


printinfo(10)
printinfo(10, 20, 30)

# Anon functions - can be created using the keyword lambda


def sum(a, b): return a + b;


print "Value of total: " sum(1, 2)

# return exits the function - and might pass back an expression to the caller


def sum(arg1, arg2):
    "Add both the parameters and return them"
    total = arg1 + arg2
    print "Inside the function : ", total
    return total


total = sum(10, 20)
print "Outside the function : ", total

# vars inside function are local, outside are global
total = 0  # Global variable


def sum(arg1, arg2):
    "Add both the parameters and return them."
    total = arg1 + arg2  # Local variable
    print "Inside the function local total : ", total
    return total


sum(10, 20)
print "Outside the function global total : ", total
