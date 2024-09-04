#using python to perform mathematical computation.

#print(x+y)                          #for addition
#print(x-y)                          #for subtraction
#print(x*y)                          #for multiplication
#print(x/y)                          #for division

#python can be used  for addition,subtraction,multiplication and division.





#precedence and associativity in python 

#  operators have different levels of precedence, which determine the order in which they are evaluated. 

#PEM-DAS        it is the algorithm to calculate the mathematical operations 
#1.     ()                                parenthesis
#2.     **                                power operator                                                          right<--left
#3.     *  /   //   %                    multiplication,division,floor division,modules                           left-->right
#4.     +   -                             addition,subtraction                                                    left-->right



#associativity in python
print(5+2*3-1+10/5)
#here both multiplication and division are present in the same statement. now we will use associativity here.

#we will move left to right in 3rd and 4th 
#we will move right to left in 2nd 

#which will come first it will be operated first.
#in that first               multiplication  >>  division  >>  addition  >>  subtraction

 



#the best way is to use parenthesis after every operator it will be time consuming but give less errors.
#if we need some fix output from the same digits parenthesis will be required.


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








#for subtraction we use - sign in between the two numbers.
print(7 - 3)

p=int(input("enter your first number:"))
q=int(input("enter your second number:"))
print(p-q)              

#we should take different variable for different calculation of different numbers.
#we can continue with same variable if want all calculation for the same number.



#for multiplication we use * sign in between the two numbers.
print(34 * 56)
print(p*q)




#for division we use / sign in between the two numbers.
print(32 / 4)
print(p / q)

#compute expression
#computeExpression.py

print((10.5 + 2*3) / (45 - 3.5))

print(2 + 8)  #addition of two numbers. +
print(9 - 5)  #subtraction of two numbers. -
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














#assignment operator
a=5
a=a+2
a+=2       #it is same as a=a+2

a=a/2
a/=2       #it is same as a=a/2


a,b,c,d=2.3,4,5









#conditional operators

# > , < , >= , <= , == , !=
a=18
print(a>18)        #it is true only when a is greater then 18.
print(a<18)        #it is true only when a is smaller then 18.
print(a<=18)       #it is true only when a is less than or equal to 18.
print(a>=18)       #it is true only when a is greater than or equal to 18.
print(a==18)       # it is true only when a  is equal to 18.
print(a!=18)       # it is true only when a is not equal to 18.
print((a+2)!=18)   #we can also add something to a while giving an operation.















#logical operators
#Python logical operators are used to combine conditional statements, allowing you to perform operations based on multiple conditions.
#1. and 
#2. or 
#3. not 



#and 
a,b=5,4
print(a>4 and b<10)    #true
print(a>4 and b<3)     #false

#for and operator if all the statement are true then it will give true,
#if one of them is false then it will give false.



#or
a,b=5,4
print(a>4 or b<10)    #true
print(a<4 or b<13)    #true

#for or operator when 1 or more statement is true it will give true.
#if no statement is true only when it will give false.

#not 
a=False
print(not(a))    #print true.


''' X                       Y                       X and Y               X or Y                 not(X)                    not(Y)
    
1.  true                   true                      true                  true                  false                     false
2.  true                   false                     false                 true                  false                     true
3.  false                  true                      false                 true                  true                      false
4.  false                  false                     false                 false                 true                      true  '''