'''1.print upper tringle matrix
2.print lower tringle matrix
3.print rhombus
4.***
    ***      -->parllelogram
      ***
5.print number pyramid
6.'''




'''n=int(input())   
for i in range(n+1):      #4th
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(n):
          print("*",end=" ")
    print()'''


'''n=int(input())   
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")       #upper
    for k in range(i+1):
          print("*",end=" ")
    print()'''


'''n=int(input())   
for i in range(n):        #lower
    for j in range(i+1):
        print(" ",end="")
    for k in range(i,n-1):
          print("*",end=" ")
    print()'''


'''n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
          print("*",end=" ")
    print() 
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(i,n-1):
          print("*",end=" ")
    print()'''


n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()