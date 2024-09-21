#what is set data type?????
# A set is a mutable data type that contains an unordered collection of items. A set is represented with { }.




# Every element in the set should be unique (no duplicates) and must be immutable (which cannot be changed).
#  But the set itself is mutable. We can add or remove items / elements from it.

# Note: Mutable data types like list, set and dictionary cannot become elements of a set.

# The set itself is mutable i.e. we can add or remove elements from the set.



#indexing is not allowed in sets because these are unordered .
# set1[2]=13


#sets are unordered so we cannot change the item because we cannot do slicing or indexing because any element has no fix order,
# they are arranged randomly.

#in python 
''' o = false and 1 = true 
                         so when we will give 1 and true in same set they will give may be true or 1 .'''



# The main uses of sets are:
#  Membership testing
# Removing duplicates from a sequence
# Performing mathematical operations such as intersection, union, difference, and symmetric difference

# Creation of sets
# 1. One way to create a set is by using built-in function set()

# Empty set
# An empty set can be created using built-in set() function.

myset = set()
print(myset)       # Result: set()
print(type(myset)) # <class 'set'>


#
# 2. Another way to create a set is to put all elements inside curly braces separated by commas.
myset1 = {1, 2, 3} 
print(myset1)       # Result: {1, 2, 3}
print(type(myset1)) # Result: <class 'set'>
# Note : Empty curly braces { } does not make an empty set in Python, it makes an empty dictionary instead. 
# Dictionary data type is introduced in the upcoming lessons.
test = { } 
print(type(test)) #Result: <class 'dict'>


set1={12,34,True,1,'hello',13.3,0,False}
print(set1)


set1.add(32)
set1.remove(12)
set1.discard(234)
#difference between discard and remove is that when item is not is present in the set and remove is used it gives key error 
# but when discard is used it print the set as it is.



print(set1)
print(len(set1))

set1.clear()   #empty set
set1.pop()     #removes any random item from this set
print(set1.pop())  # show the removed item




#we can only add only immutable items in sets like tuple,string , int , float etc.
#we cannot add mutable items like list.