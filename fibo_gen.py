def fibo(n):
    i=1
    a=0
    b=1
    f=0
    while(i<=200):
        c=a+b
        a=b
        b=c
        if n==c:
            f=1
            break
        else:
            pass
        i=i+1
    if f==1:
        return "Yes"
    else:
        return "No"

n=int(input("Enter a number to check if it is a part of the fibonacci sequence: (other than 0) "))
s=fibo(n)
print(s)

