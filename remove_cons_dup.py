l=list()
l=input("Enter your elements:\n").split()
n=[]
for i in range(len(l)):
    l[i]=int(l[i])
i=0
while(i<len(l)-1):
    if l[i]!=l[i+1]:
        n.append(l[i])
    i=i+1
n.append(l[-1])
print(n)

