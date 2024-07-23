''' reverse of a number '''
n=int(input())
s=""
while n>0:
    r=n%10
    s=s+str(r)

    n=n//10
#print(s) 
#print(type(s)) 
#ans=int(s)
#print(ans)
print(int(s)) 
print(type(s)) 
#print(type(ans)) 