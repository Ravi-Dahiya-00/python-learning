total=0
for i in range(0,101):
    if i%2==0:
        total=total+i
    elif i==1:
        total=total+i
    elif i==100:
        total=total+i
print(total)