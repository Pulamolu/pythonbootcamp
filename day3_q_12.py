'''max element in a given list'''
'''m=list(map(int,input().split(" ")))
print(max(m))'''




m=list(map(int,input().split(" ")))
res=m[0]
for i in range(len(m)):
    if(m[i]>res):
        res=m[i]
print(res)        
