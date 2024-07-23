#list is ordered and sets are unordered


'''my_list=[1,2,3,4]
print(my_list)
print(*my_list)   # *is used for removing the square brackets and comma 
print(*my_list,end="@")
my_list.append(99999)    #default insert in the last
print(*my_list)
my_list.insert(0,999)     #insert at specific position
print(*my_list)
print(len(my_list))
my_list.pop()
print(*my_list)   #defelt last element will pop
my_list.pop(2)       #pop at specific index
print(*my_list) 
my_list_2=[5,6,7,8]
#new_list=my_list+my_list_2
#print(*new_list)
new_list=my_list.copy()
new_list.pop()
print(*new_list)
print(*my_list)
my_list=[1,2,3,-13,14,-54,-30,4,2,6,8,999,2]
cnt=my_list.count(2)
print(cnt)
#sorting
my_list.sort()     #defelt quick sort (nlogn)
print(my_list)
print(*my_list)



#pop
my_list.pop()
print(*my_list)
my_list.pop(5)
print(*my_list)
my_list.pop(4500)
print(*my_list)'''




'''my_list=list(map(int,input().split(" ")))    
my_list=list(map(int,input().split("@")))    '     #list-->tye casting,map-->morethen one element,split-->
my_list=list(map(int,input().split(",")))
my_list.append(99)
my_list.insert(0,69)      #error
print(*my_list)'''
'''#1.append 2.pop 3.sort 4.print gud mrng,length of the string 
my_list=list(map(int,input().split(" "))) 
choice=int(input())
if (choice==1):
    my_list.append(99)
    print(*my_list)
elif (choice==2):
    my_list.pop()
    print(*my_list)
elif(choice==3):
    my_list.sort()    
    print(*my_list)
else:
    print(f"good morning {len(my_list)}")'''


