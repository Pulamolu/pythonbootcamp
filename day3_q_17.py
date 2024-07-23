'''find the duplicates in an array
using membership operators-->in'''



m=list(map(int,input().split(" ")))
'''for i in range(0,len(m)):
    for j in range(i+1,len(m)):
        if(m[i]==m[j]):
            print(m[j],end=" ")'''
    

n=[]
for i in m:
    if (i not in n):
        n.append(i)
print(n)