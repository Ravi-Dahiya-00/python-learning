''' conditional statements are the statements where we write some condition
 if it happens write these 
 else write this.'''

height=int(input("enter your height in feet:" ))

#it can also be written as
#if(height>3):
if height>3:
    print("buy Token")
    print("now you can in metro")
else:
    print("no token required")
print("this is not the part of indentation so it will be printed if any of statement will be printed")
print("it can not be used in between if and else condition because it will break the condition statement after if condition  and no else condition will be taken after that if.")







number= int(input("enter a number"))

if number%2==0:
    print("it is even number")
else:
    print("it is odd number")











#nested if else and elif

#problem
#can ride if height is greater than 3
#pay 150rs if age is less than 12
#pay 250rs if age is less than or equal to 18
#pay 500rs if age is greater than 18
#if height is less then 3 than cannot ride


height=int(input("Enter your height:"))
if height>3:
    print("you can ride")
    age=int(input("enter your age"))
    if age<12:
        print("pay 150 rs")
    elif age<=18:
        print("pay 250 rs")
    else:
        print("pay 500 rs")
else:
    print("you cannot ride")
print("thank you for visiting our shop")


#1.we can use as many elif as many condition we want to make under the if condition.

'''2.we can also use as many if condition as many we want to make a condition it will work properly but it is not right way to do this because 
   it will scan all the if conditions and it is not a efficient.'''
