l=[1,2,3,4,5,4,5,6,7,8,9,10,5,11,12,13,14,15,16,17]
n=[]
m=[]
for i in range(len(l)):
    if l[i] not in n and i!=len(l)-1:
        n.append(l[i])
    elif i==len(l)-1:
        if l[i] not in n:
            n.append(l[-1])

    else:
        if len(n)>len(m):
            m=n.copy()
            n=[]
if len(n)>len(m):
    m=n.copy()

print(m)

