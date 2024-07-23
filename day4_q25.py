'''lcm '''
a=int(input())
b=int(input())
n=a*b
while b!=0:
    a,b=b,a%b
lcm=(n)//a
print(lcm)