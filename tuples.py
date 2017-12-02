tup1 = ()  # empty tuple
tup1 = (50,)  # tuple with 1 value

# tuples can be created by values seperated by comma stored in a variable
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
tup3 = "a", "b", "c", "d"

# accessing values in tuple
print("tup[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# updating tuple
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2  # concatenates the two tuples above
print tup3
# deleting tuple elements
tup = ('physics', 'chemistry', 1997, 2000)
print tup
del tup  # deletes instantiated tuple tup
print "After deleting tup : "
print tup  # will throw an error because tuple tup is no longer defined

# tuple operations
len(tup)  # length
tup1 + tup2  # concatenation
tup1 * 4  # repetition
12 in tup1  # binary find (returns T/F)
for x in tup3:
    print x  # goes through tuple tup3 and prints each of the elements

# tuple indexing, slicing and matrixes
L = ('spam', 'Spam', 'SPAM!')
L[2]  # returns 'SPAM!'
L[-2]  # returns 'Spam'
L[1:]  # returns ['Spam', 'SPAM!']

# () - delimiters are not mandatory

cmp(tup1, tup2)  # compares elements of both tuples
len(tup1)  # length of tuple
max(tup1)  # returns item with max value
min(tup1)  # returns intem with min value
tuple(seq)  # converts list to tuple
