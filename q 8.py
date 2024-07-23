''' space seperated int list find the avg of elements present in the even index'''



'''m=list(map(int,input().split(" ")))
sum=0
count=0
n=len(m)
for i in range(len(m)):
    if(i%2==0):
        sum+=m[i]
        count+=1
print(sum/count)        '''

#average of all the numbers

m=list(map(int,input().split(" ")))
sum=0
count=0
n=len(m)
for i in range(len(m)):
    sum+=m[i]
    count+=1
print(sum/count)  