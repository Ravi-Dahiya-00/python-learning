#list objects are mutable once we create list objects we can perform any changes in that object.

#if content is changing we can go for a list.

#list objects can not used as key for dictionaries because key should be hashable and immutable.



# Here is a list of operations that are possible on a list sequence:

# Operations	Example	Description


# Create a List	
a = [2 ,3, 4, 5, 6, 7, 8, 9, 10]
print(a) # [2 ,3, 4, 5, 6, 7, 8, 9, 10]
# Create a comma separated list of elements and assign to variable 'a'




# Indexing	
print(a[0])    # 2
print(a[-1])   # 10
# Access the item at position '0'
# Access the last item using negative indexing



# Slicing	
print(a[0:3]) # [2, 3, 4]
print(a[0:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Print a part of list starting at index '0' till index '2'
# Print a part of the list starting at index '0' till the end of list



# Concatenation	
b = [20, 30]
print(a + b)  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
# Concatenate two lists and display its output



# Updating	
a[2] = 100
print(a)   # [2, 3, 100, 5, 6, 7, 8, 9, 10]
# Update the list element at index 2



# Membership	
5 in a     # True
102 in a   # False

# Returns True if element is present in list.

# Otherwise returns false.

# Comparison	
a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 3, 4]
a == b     # False
# Returns True if all elements in both lists are same.


# Otherwise returns false
# Repetition	
a = [1, 2, 3]
print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] 
# Here the * operator repeats a list for the given number of times.
