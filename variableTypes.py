# Values to variables
inte = 100  # integer variable type
fl = 100.0  # floating variable type
st = 'john'  # string variable type

# Multiple Assignment
a = b = c = 1  # all three variables (a,b,c) have a value of 1
a, b, c = 1, 2, 'john'  # value of integer 1 to a, integer 2 to b, and string 'john' to c

# 5 data types

# Numbers
var1 = 1
var2 = 10
var3 = 100  # three varialbes instantiated with respective integer values
del var1
del var2, var3  # can delete one or more variables in a line at a time
# 4 numerical variable types
a = 10  # integer variable type
b = 5200000L  # 'L' indicates long integer variable type (can be in octal or hexadecimal)
c = 0.5  # float variable type
d = 5.j  # complex number with imagianry component

# Strings
strng = "Hello World!"
print strng  # displays entire string
print strng[0]  # displays first character of string
print strng[2:5]  # displays third through the fifth character but not the fifth
print strng[2:]  # displays string from the third character onwards
print strng * 2  # displays the string two times
print strng + "TEST"  # displays the string and the specified characters after

# Lists (similar to arrays but each item can be of a different data types
lsts = ['abcd', 786, 2.23, 'john', 70.2]
smalllsts = [123, 'john']
print lsts  # prints the entire list
print lsts[0]  # prints first element in the list
print lsts[1:3]  # prints elements from the second to the third items but not the third
print lsts[2:]  # prints all the elements starting from the third item
print smalllsts * 2  # prints smalllsts twice
print lsts + smalllsts  # prints the two lists

# Tuples ("read-only" lists)
tuples = ('abcd', 786, 2.23, 'john', 70.2)
smalltuple = (123, 'john')
print tuples  # prints the entire list
print tuples[0]  # prints first element in the list
print tuples[1:3]  # prints elements from the second to the third items but not the third
print tuples[2:]  # prints all the elements starting from the third item
print smalltuple * 2  # prints smalllsts twice
print tuples + smalltuple  # prints the two lists

# tuple[2] = 1000 is invalid as a tuple cannot be updated
# list[2] = 1000 is valid however

# Dictionary
dictnry = {}
dictnry['one'] = "This is one"
dictnry[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print dictnry['one']  # Prints value for 'one' key
print dictnry[2]  # Prints value for 2 key
print tinydict  # Prints complete dictionary
print tinydict.keys()  # Prints all the keys
print tinydict.values()  # Prints all the values
