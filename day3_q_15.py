''' 1. even r odd --
2.greatest of 3 numbers --
3.sum of all the elements in the array --
4***.find peek element in an array***(imp)
5.max element in an array  --
6.second max element in an array
7.reverse an array with out using built in function  --
8.sum of squares of given number  --
9.sum of squares of even and odd digits  --
10.check given num is palindrome using while loop  --
11.print the frst n febinocci series  --
'''




'''n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")   '''


'''n=list(map(int,input().split(" ")))       #even numbers-1
for i in range(0,len(n)):
    if(n[i]%2==0):
        print(f"the even numbers are {i}",end=" ")'''




'''n=list(map(int,input().split(" ")))
for i in range(0,len(n)):               #odd numbers-1
    if(n[i]%2!=0):
        print(f"the odd numbers are {i}")   '''




'''a=int(input())
b=int(input())
c=int(input())
if (a>b and b<c):
    print(b)            #greatest number-2
elif(a<c and b<c):
    print(c)
else:
    print(a)  '''



'''n=list(map(int,input().split(" ")))
sum=0
for i in range(0,len(n)):      #sum of array-3
    sum=sum+n[i]
print(sum)'''




'''m=list(map(int,input().split(" ")))
res=m[0]
for i in range(len(m)):        #max num-5
    if(m[i]>res):
        res=m[i]
print(res)   '''




'''n=list(map(int,input().split()))
rev=[]
for i in range(len(n)-1,-1,-1):          #rev of array-7
    rev.append(n[i])
print(*rev)'''




'''n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r**2     #sum of squares of a num-8
    n=n//10
print(sum)'''




'''n=list(map(int,input().split()))
e=0
o=0
for sub in n:
    for ele in str(sub):
        if int(ele) % 2 == 0:       #sum of squares of even and odd digits-9
            e+= int(ele)
        else:
            o+= int(ele)
print(str(o))
print(str(e))'''





'''n=int(input())
temp=n
s=0
while n>0:
    r=n%10
    s=s*10+r    #palindrome-10
    n=n//10
if(temp==s):
    print("palindrome")
else:
    print("not an palindrome")'''



'''n=list(map(int,input().split(" ")))
count=0
for i in range(1,len(n)-1):
    if(n[i]>n[i+1] and n[i]>n[i-1]):   #all the peek elements(imp)
        count=i
        #break
        print(n[count],end=" ")
#print(n[i])
    '''




'''n=list(map(int,input().split(" ")))
count=0
for i in range(1,len(n)-1):
    if(n[i]>n[i+1] and n[i]>n[i-1]):   #frst the peek elements
        count=i
        break
print(n[count],end=" ")'''


'''n=list(map(int,input().split(" ")))
count=0
for i in range(1,len(n)-1):
    if(n[i]>n[i+1] and n[i]>n[i-1]):   #frst the peek elements
        count=i
        #break
        #print(n[count],end=" ")
if(n[-1]>n[-2] and n[-1]>count):   
    count=len(n)-1
print(n[count],end=" ")'''


'''febinocci series
n=int(input())
t1=0
t2=1 
t3=0
for i in range(0,n):
    print(t3)
    t1=t2 
    t2=t3
    t3=t1+t'''



n=list(map(int,input().split(" ")))
a=n[0]
for i in n:
    if a<i:
        a=i
m=n[0]
for j in n:
    if m<j and j<a:
        m=j
print(m)
