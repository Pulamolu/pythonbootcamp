'''check how many vowels are present in the given string'''

'''n=['a','e','i','o','u']
count=0
a=input()
b=a.lower()
for i in b:
    if i in n:
        count+=1
print(count)  '''      


''' to print the count of consonents and vowels'''


'''n=['a','e','i','o','u']
c="bcdfghjklmnpqrstvwxyz"
count=0
d=0
a=input()
b=a.lower()
for i in b:
    if i in n:
        count+=1
print(count)
for i in b:
    if(i in c):
        d+=1
print(d)'''



'''print the all lettres of vowel and consonent
n=['a','e','i','o','u']
c="bcdfghjklmnpqrstvwxyz"
count=0
d=0
a=input()
b=a.lower()
for i in b:
    if i in n:
        count+=1
        print(i)
for i in b:
    if(i in c):
        d+=1
        print(i)'''
#or

n=['a','e','i','o','u']
c="bcdfghjklmnpqrstvwxyz"
count=""
a=input()
b=a.lower()
for i in b:
    if i in n:
        count+=i
for i in b:
    if(i in c):
        count+=i
print(count,end=" ")