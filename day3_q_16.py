'''find the missing num in an array'''


m=list(map(int,input().split(" ")))
sum=0
sum1=0
miss=0
for i in range(1,11):
    sum=sum+i
for i in range(0,len(m)):
    sum1=sum1+m[i]
    miss=sum-sum1
print(miss)