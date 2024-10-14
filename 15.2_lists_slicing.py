# List slicing extracts a subset of elements from a list to create a new list. The syntax for List slicing:


'''
Listname[start:stop]
Listname[start:stop:steps]
Default start: 0
 Default stop: n-1
[:] prints the whole list
[2:2] creates an empty slice
'''

# Let's consider a = [9, 8, 7, 6, 5, 4], observe the following examples:

a = [9, 8, 7, 6, 5, 4]
# Slices	Example	Description
print(a[0:3])	
# [9, 8, 7]	Print a part of list from index 0 to 2

print(a[:4]	)
# [9, 8, 7, 6]	Default start value is 0.
# Prints the values from index 0 to 3


print(a[1:]	)
# [8, 7, 6, 5, 4]	Prints values from index 1 onwards


print(a[:]	)
# [9, 8, 7, 6, 5, 4]	Prints the entire list


print(a[2:2])
# [ ]	Prints an empty slice


print(a[0:6:2])
# [9, 7, 5]	Slicing list values with step size 2


print(a[::-1])
# [4, 5, 6, 7, 8, 9]	Prints the list in reverse order


print(a[-3:])
# [6, 5, 4]	Prints the last 3 items in list


print(a[:-3])
# [9, 8, 7]	Prints all except the last 3 items in list