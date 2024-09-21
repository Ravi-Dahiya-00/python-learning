#basic syntax of for loop

'''for var_name in sequence:
      statement(s)      '''

names = [ "ravi","rahul","jatin","ram"]
for name in names :
    print(name)
    if name:
        print(f"hii {name}")


#it will print name in systematic order one by one and not randomly.
#this is known as iteration.



numbers=[2,3,4,5,6]
squares=[]
for i in numbers:
    square=i**2
    squares.append(square)
    print(squares)                     #this will print one by one with every condition 
print("the list of squares is : ",squares)                         #this will print only one time after completion of for loop.