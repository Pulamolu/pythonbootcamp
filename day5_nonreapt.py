'''print the unique char in a string'''


n=['a','e','i','o','u']
c="bcdfghjklmnpqrstvwxyz"
count=""
a=input()
b=a.lower()
for i in b:
    if(i not in count):
        count+=i
print(count)