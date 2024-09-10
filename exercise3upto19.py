# #we have to take a two or more digit number from the user and add all the digits of the number by using addition.

# x=input("enter a two digit number:")
# a=x[0]
# b=x[1]

# sum=int(a)+int(b)
# print(sum)








# # BMI calculator using for finding underweight or overweight.



# #formula=(weight/height**2)

# #taking users weight and height input
# weight=float(input("enter your body weight in kilograms:"))
# height=float(input("enter your body height in meter:"))

# #now we have both value of weight and height but remember that these values are in string . first convert them into int value .
# #we can also convert  them directly using int while making BMI operator 
# BMI=weight/height**2
# print(BMI)

# if BMI <18.5:
#     print(f"your BMI is {BMI} and you are underweight.")
# elif BMI<25 :
#     print(f"your BMI is {BMI} and you have normal weight.")
# elif BMI<30 :
#     print(f"your BMI is {BMI} and you are overweight.")
# elif BMI<35 :
#     print(f"your BMI is {BMI} and you are obese.")
# else:
#     print(f"your BMI is {BMI} and you are clinically obese.")








#finding leap year using if elif and else condition.

#input of  a year
#if year is divisible 4.
     #if it is divisible 4 
     # then check it is it divisible by 100 or not.
     #if no then it is nota ;leap year.
     #if yes then check is it divisible by 400.
     #if no then not a leap year
     #if yes then it is a leap year.
#if year is not completely divisible by 4 then print it is not a leap year.

year=int(input("enter a year : "))
if year%4==0 :
    if year%100==0 :
        if year%400==0 :
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")
    

      