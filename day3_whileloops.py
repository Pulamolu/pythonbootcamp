a=int(input())
res=0
while a>0:
    rem=a%10
    res=res+rem   #imp line
    a=a//10
print(res)    