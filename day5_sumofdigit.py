'''sum of digits in string'''


'''n=['a','e','i','o','u']
c="bcdfghjklmnpqrstvwxyz"
count="0123456789"
ans=0
a=input()
b=a.lower()
for i in b:  
    if i in count:
        ans+=int(i)
print(ans)'''



'''sum of digits using ascii values'''
b=input()
sum=0
for i in b:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)




