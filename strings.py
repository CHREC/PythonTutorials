# string vals
var1 = 'Hello World!'
var2 = 'Python Programming'
print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]
print "Updated String:- ", var1[:6] + 'Python'

# escape characters
print '\a'  # bell or alert
print '\b'  # backspace
print '\cx'  # control x
print '\C-x'  # control x
print '\e'  # escape
print '\f'  # formfeed
print '\M-\C-x'  # meta-control-x
print '\n'  # new line
print '\nnn'  # octal notation
print '\r'  # carraige return
print '\s'  # space
print '\t'  # tab
print '\v'  # vertical tab
print '\x'  # character x
print '\xnn'  # hexadecimal notation

# string operators
a = 'Hello'
b = 'Python'
print a + b  # string concatenation
print a * 2  # string repeat
print a[1]  # string subset or "slice"
print a[1:4]  # strin subset or "slice range"
a in b  # membership test will return false
a not in b  # membership test will return in true
print r'\n'  # raw string - ignores escape character
print R'\n'  # raw string - ignores escape character

# string formatting operators
print 'My name is %s and height is %d feet and %d inches' % ('Sid, 5, 8')
print '%c'  # character
print '%s'  # string - convert using str() before doing this
print '%i or %d'  # signed decimal integer
print '%u'  # unsigned decimal integer
print '%o'  # octal integer
print '%x or %X'  # hexadecimal integer in lowercase or uppercase respectively
print '%e or %E'  # exponential notation with lowercase or uppercase e respectively
print '%f'  # floating point real number
print '%g or %G'  # shorter of %f and % e or %f and %E respectively

# other arguments
# *: specifies width or precision
# -: left justification
# +: displays the sign
# <sp>: blank space before the positive number
# #: add octal leading zero or hexadec leading '0x' or '0X'
# 0: pad left with zeros instead of spaces
# %: %% results in single literal (%)
# (var): mapping variable
# m.n.: minimum total width; number of digits to display after point

# triple quotes
para_str = """is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up."""
print para_str
print '\\'  # prints '\'
print u'Hello World!'  # prints string as unicode

# string methods
capitalize()  # capitalizes first letter of String
center(width, fillchar)  # returns string with original string centered to a total of width col.
count(str, beg=0, end=len(string))  # counts number of times str occurs in string
decode(encoding='UTF-8', errors='strict')  # decodes string using codec reg for encoding
encode(encoding='UTF-8', errors='strict')  # returns encoded string
# determines if string or substring of string ends with suffix
endswith(suffix, beg=0, end=len(string))
# T/F
expandtabs(tabsize=8)  # expands tabs in string to multiple spaces (def=8/tab)
find(str, beg=0, end=len(string))  # determines if str occurs in string or sub of string
index(str, beg=0, end=len(string))  # same as find() but raises exception if string is not found
isalnum()  # returns true is string has at least 1 character is alphanumeric
isalpha()  # returns true if strinf has at least 1 character is alphabetic
isdigit()  # returns true is string contains digits
islower()  # returns true is string has at least 1 lower cased character
isnumeric()  # returns true if a unicode string contains only numeric characters
isspace()  # returns true if string contains only whitespace characters
istitle()  # retursn true if strinf is properly "titlecased"
isupper()  # returns true if string has at least 1 upper cased charater
join(seq)  # concatenates string representations of elements in seq into a String
len(string)  # returns lngth of a String
ljust(width, [, fillchar])  # returns space-padded string with oriinal string left-justified
lower()  # converts all uppercase letters in string to lowercase
lstrip()  # removes all leading whitespace in String
maketrans()  # returns a translation table to be used in translate function
max(str)  # returns the max alphabetical char from str
min(str)  # returns the min alphabetical char from str
replace(old, new[, max])  # replaces all occurrances of old in string with new
rfind(str, beg=0, end=len(string))  # same as find() but searches backwards
rindex(str, beg=0, end=len(string))  # same as index(), but search backwards
rjust(width, [, fillchar])  # returns a space-padded string with the original string right-justified
rstrip()  # removes all trailing whitespace of string
split(str="".num=string.count(str))  # splits string according to delimiter str and returns substrs
splitlines(num=string.count('\n'))  # splits string at all newlines and returns a lists
startswith(str, bed=0, end=len(string))  # determines if string or substring starts with str
# T/F
strip([chars])  # performs both lstrip() and rstrip() on string
swapcase()  # inverts case for all letters in string
title()  # returs titlecased version of string
# translates string according to translation table removing those in del string
translate(table, detelechars="")
upper()  # converts lowercase letters in string to uppercase
zfill(width)  # returns string leftpadded with 0s to a total of width characters
# intended for numbers--and retains any sign given (less one zero)
isdecimal()  # returns true if unicode string contains only decimal characters
