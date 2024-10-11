for i in range(1,20000000000000):
    if i==2:
        print(2)
    elif i==3:
        print(3)
    elif i==5:
        print(5)
    elif i%2==0 or i%3==0 or i%5==0:
       pass
    else:
        print(i)
import math