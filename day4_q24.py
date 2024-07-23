'''gcd of a number
euclidean algorithm'''


a=int(input("enter the frst no: "))
n=int(input("enter the second no: "))
while n!=0:
    a,n=n,a%n
    print("gcd of 2 numbers are: ",a)