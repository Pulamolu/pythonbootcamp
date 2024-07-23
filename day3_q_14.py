''' replace the elements in an array with avg of max and min elements'''


m=list(map(int,input().split(" ")))
max=m[0]
min=m[0]
for i in range(len(m)):
    if(m[i]<min):
        min=m[i]
#print(min)  
for i in range(len(m)):
    if(m[i]>max):
        max=m[i]
#print(max)
avg=(max+min)//2
#print(avg)  
for i in range(len(m)):
    m[i]=avg
print(m)    