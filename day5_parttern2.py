''' *******
* ******
** *****
*** ****
**** ***
***** **
****** *'''



n=int(input())
for i in range(1,n):
    for j in range(1,n):
        if i==j:
           print(" ",end="")
        else:   
            print("*",end="")
    print()