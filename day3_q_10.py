''' find the elements that is present in k+n index
k is given by user where k=3 n=2 i/p are 3 6 8 4 61 2 and the o/p is 2
k=3 n=4 i/p are 80 70 54 36 72 o/p is error'''

        
        
'''l=list(map(int,input().split())) buikyu
n=int(input())
k=int(input())
length=k+n  
if(length>k+n):
    print("index bound errror")
else:
    for i in range(0,len(list)):
        print(list[k+n],end="")
        break'''
       

l=list(map(int,input().split())) 
n=int(input())
k=int(input())
print(l[k+n])
