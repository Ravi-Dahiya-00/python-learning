#using python to perform mathematical computation.

#print(x+y)                          #for addition
#print(x-y)                          #for subtraction
#print(x*y)                          #for multiplication
#print(x/y)                          #for division

#python can be used  for addition,subtraction,multiplication and division.





#precendence and associativity in python 

#  operators have different levels of precedence, which determine the order in which they are evaluated. 

#PEMDAS
#1.     ()                                paranthesis
#2.     **                                power operator                                                          right<--left
#3.     *  /   //   %                    multiplication,division,floor division,modules                          left-->right
#4.     +   -                             addition,subtractionleft-->right                                       left-->right


print(5+2*3-1+10/5)
#here both multiplication and division are present in the same statement. now we will use associativity here.

#we will move left to right in 3rd and 4th 
#we will move right to left in 2nd 

#which will come first it will be operated first.
#in that first multiplication>>division>>addition>>subtraction





#the best way is to use parenthisis after every operator it will be time consuming but give less errors.
#if we need some fix output from the same digits parenthisis will be required.


#if we want 11 from the same digits we will use it like this:
print(((((10+5)/3)+5)+2)-1)










#for addition we use + sign in between the two numbers.
print(5 + 6)

x=int(input("enter your first number:"))
y=int(input("enter your second number:"))
print(x+y)



#this + is used to concatenate a string and a number here.
# + can also be used for concatenate a string and a number.
b=1
print("b=" + b)








#for substraction we use - sign in between the two numbers.
print(7 - 3)

p=int(input("enter your first number:"))
q=int(input("enter your second number:"))
print(p-q)              

#we should take diiferent variable for different calculation of different numbers.



#for multiplication we use * sign in betwwen the two numbers.
print(34 * 56)
print(p*q)

#we can continue with same variable if want all calculation for the same number.



#for division we use / sign in between the two numbers.
print(32 / 4)
print(p/q)

#compute expression
#computeExpression.py

print((10.5 + 2*3) / (45 - 3.5))

print(2 + 8)  #addition of two numbers. +
print(9 - 5)  #substraction of two numbers. -
print(5 * 3)  #multiplication of two numbers. *
print(5 / 3)  #division of two numbers. /
print(
    7 // 2
)  #floor division of two numbers. //    used to calculate approx division of two numbers.
print(
    5 % 3
)  #modulus of two numbers. %    used to calculate reminder of two numbers.
print(
    5**3
)  #exponential of two numbers. **    used to calculate power of two numbers.

