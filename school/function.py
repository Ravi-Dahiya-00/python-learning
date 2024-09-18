a=input("enter your name : ")
def wish(a):
    print("HELLO",a)
wish(a)



def add(x,y):
    return x+y
result=add(10,20)
print("the result is " , result)
print("the sum is " , add(100,200))


def even_odd(num):
    if num%2==o:
        print(num,"is Even number")
    else:
        print(num,"is odd number") 
        




def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(100,50)
print("the sum is:",x)
print("the sub is:",y)



#VARIABLE LENGTH ARGUMENTS:
def sum(*n):
    total=0
    for n1 in n:
          total =total+n1
          print(total)



def f1(n1,*S):
    print(n1)
    for s1 in S:
        print(s1)

























































































































































