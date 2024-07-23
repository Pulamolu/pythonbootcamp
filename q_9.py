'''1.to find the area of a circle
 2.perimeter of the circle
 3.to find area of a triangle
 4.perimeter of a triangle
 5.prime num in sqrt root method'''

 

'''n=int(input())
area=3.14*n*n
print(f"the area of the circle is {area}")



n=int(input())
perimeter=2*3.14*n
print(f"the perimeter of the circle is {perimeter}")



n=int(input())
m=int(input())
area=0.5*n*m
print(f"the area of the triangle is {area}")



a=int(input())
b=int(input())
c=int(input())
perimeter=a+b+c
print(f"the perimeter of the triangle is {perimeter}")'''  



from math import sqrt
n = int(input())
flag = 0
if(n > 1):
	for k in range(2, int(sqrt(n)) + 1):
		if (n % k == 0):
			flag = 1
		break
	if (flag == 0):
		print(" is a Prime Number")
	else:
		print(" is Not a Prime Number")
else:
	print(" is Not a Prime Number")   