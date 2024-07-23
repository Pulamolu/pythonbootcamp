'''leep year'''


'''n=int(input())
if(n%400==0 or (n%4==0 and n%100!=0)):
    print("leep year")
else:
    print("not a leep year")'''



n=int(input())
m=int(input())
for i in range(n,m+1):
    if i%400==0 or (i%4==0 and i%100!=0):
        print(i,end=" ")
    