#2.
tuple1 = ('parrot', 'sparrow')
print(type(tuple1))

print(tuple1)
#tuple is a ordered collection of different data types.it can be changed these are immutable.
#we cannot compare any element in the mix tuple like using minimum or maximum function

print(len(tuple1))

tuple2=(11,"ravi",10.23,True,11)
print(tuple2[1])    #indexing any element 
print(tuple2[-2])   # negative indexing
print(tuple2[1:])   #tuple slicing
print(tuple2[::2])


#occurrence of any element in any tuple:
print(tuple2.count(11))


print(tuple2.index(11))

tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple3[1])


tuple7=tuple1 + tuple2
print(tuple7)               #for concatenating tuple1 and tuple2 elements in a single tuple.

tuple4=("ravi")       #this is not a tuple this is a string 
print(type(tuple3))

tuple5=("ravi",)      #if want it to convert into a tuple we have to put 1 comma after this.
print(type(tuple4))


tuple11=(10,)*5        
print(tuple11)        #print 10 5 times.




#converting of a list into a tuple
list1=[1,2,3,5,6,78,9,7]
print(tuple(list1))