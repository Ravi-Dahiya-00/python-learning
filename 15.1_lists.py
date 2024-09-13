#1.
list1 = [8, 2.3, [-4, 5], ['apple', 'banana']]
print(
    list1
)  #list is a ordered collection of different data types and enclosed by square brackets and separated by commas.it can be changed these are mutable.
#we can store int,str,boolean,float and many more data types in list. 




#the append() method is used to add items to the list.



chars = ['a', 'b', 'c', 'd']
chars.append("abcd")
print(chars) # will print output as follows

#Output :
['a', 'b', 'c', 'd', 'abcd']









# The extend() method is used to add items of one list to be added as individual items of another list.

chars = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3]
chars.extend(list2)
print(chars) # will print output as follows

# Output : 
['a', 'b', 'c', 'd', 1, 2, 3]

# Note : Closely observe that the items of list2 are added as individual items to the chars list







#to change any number in the line with another number

# chars['a']=['hii']

# print(chars)


chars[1:3]=['hii','hello']








#Slicing and indexing are two fundamental concepts in Python.


# They help you access specific elements in a sequence, such as a list, tuple or string.


#indexing in python:
'''In Python, indexing starts from 0, which means the first element in a sequence is at position 0,
 the second element is at position 1, and so on.

To access an element in a sequence, you can use square brackets [] with the index of the element you want to access.'''

my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[0]) # output: 'apple'
print(my_list[1]) # output: 'banana'


#negative indexing
print(my_list[-2])    #it starts from -1

# Slicing in Python
'''Slicing is the process of accessing a sub-sequence of a sequence by specifying a starting and ending index. 
In Python, you perform slicing using the colon : operator.'''

my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[1:3]) # output: ['banana', 'cherry']  
         # 3 doesn't mean it will print upto 3rd element this three is length but 1 is starting element.



my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[:2]) # output: ['apple', 'banana']
print(my_list[2:]) # output: ['cherry', 'date']



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = numbers[::2]
print(odd_numbers) # output: [1, 3, 5, 7, 9]

#  The ::2 slice means that we are selecting every other element starting from the first element,




# Suppose we have a list of numbers and we want to modify the values of some of the elements in the list. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1:4] = [10, 20, 30]
print(numbers) # output: [1, 10, 20, 30, 5, 6, 7, 8, 9]


# We could also insert new elements into the list using slicing as follows:
numbers.insert(2,45)
print(numbers)



numbers[4:4] = [40, 50]
print(numbers) # output: [1, 10, 20, 30, 40, 50, 5, 6, 7, 8, 9]







# Suppose we have a 2D list representing a table of data, and we want to extract a particular column from the table.
#  We can do this using list comprehension and indexing as follows:

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column = [row[1] for row in data]
print(column) # output: [2, 5, 8]

column_0 = [row[0] for row in data]
column_2 = [row[2] for row in data]
print(column_0) # output: [1, 4, 7]
print(column_2) # output: [3, 6, 9]





#extended slicing 
#for skipping any characters in sequence we use this 
list=[1,2,3,4,5,6,7,8,9]
print(list[0:6:2])    #it will do it upto 6 characters and skip every 2nd word
print(list[::3])      #it will do complete this thing with complete list









list.sort()
print(list)



list.reverse()
print(list)         #dont work in for loop
print(list[::-1])         #it will work every time 



print(min(list))


print(max(list))




list.remove(2)
print(list)             #it will remove only first 2 from the code


list.pop()                 #we can also provide which element we want to remove.   pop(2)
print(list)                 #it will return all the elements
print(list.pop())               #it will print which item is removed 
