''' cyclic production of an array
print the element in the particular index and do cyclic manner'''
 

k=int(input())
my_list=list(map(int,input().split(" ")))
len=len(my_list)
rem=k%len
if(rem==0 and rem!=0):
     print("error")
else:
    print(my_list[rem])



'''k=int(input())
my_list=list(map(int,input().split(" ")))
idx=k%len(my_list)
print(my_list[idx])'''