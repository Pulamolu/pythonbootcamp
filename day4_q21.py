'''password verifier:
mr.x is trying to create a new password for his insta acc these are the required conditions for
creating a new password
cond 1:min length is 8 and max length is 15
cond 2:only @,/is must allowed in the pass
cond 3:no spaces are allowed
cond 4:only alpha numeric are allowed
we should print weak if len is =8 medium len is btw 8-12 strong if len is btw 12-15'''

n=input()
l=len(n)
a="@" or "/"
for i in a:        
    if " " not in n:
        if(l==8):
            print("week password")
        elif(l>8 or l==12):
            print("medium password")    
        elif(l>12 or l==15):
            print("strong password")
    else:
        print("please follow all the conditions")
 