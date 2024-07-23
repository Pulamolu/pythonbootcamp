'''frst num should store and reverse the num'''
#home work


n=['a','e','i','o','u']
c="bcdfghjklmnpqrstvwxyz"
count="0123456789"
ans=0
temp=" "
a=input()
b=a.lower()
for i in b:
    if i in count:
        temp+=i
t=int(temp)
r,d=0,0
while t>0:
    d=t%10
    r=r*10+d
    t=t//10
print(str(r))