'''prime number
2.to print all the prime numbers in a given range using square method--
(append i)
'''




'''#a=list(map(int,input().split()))
a=int(input())
r=a**0.5
count=0
if a==1:
    print("not a prime")
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break
if count==0:
    print("prime")
else:
    print("not prime")'''


n=int(input())
m=int(input())
for i in range(n,m+1):
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            break
    else:
        print(i)
