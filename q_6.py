''' count even and odd elements
space seperated input from user and print alternate elements '''



'''n=int(input())
for i in range (1,n,2):
    print(i,end=" ")'''



my_list=list(map(int,input().split(" "))) 
for i in range (0,len(my_list),2):      #for odd num
    print(my_list[i],end=" ")



my_list=list(map(int,input().split(" "))) 
for i in range (1,len(my_list),2):      #for even num
    print(my_list[i],end=" ")
