def isprime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    return c==0

N=int(input("Enter no. of hours in a day: "))
P=int(input("Enter no. of parts in a day: "))
k=N//P
l,nums=[],[]
c=0
for i in range(2,k+1):
    m,v=P,0
    while m!=0:
        m-=1
        l.append(isprime(i+k*v))
        nums.append(i+k*v)
        v+=1
    if False in l:
        l=[]
        nums=[]
    else:
        c+=1
        print(nums)
        l=[]
        nums=[]
print(c)




