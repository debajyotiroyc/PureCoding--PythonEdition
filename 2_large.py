l=input("Enter the numbers:\n").split()
for i in range(len(l)):
    l[i]=int(l[i])
l.sort(reverse=True)
s,s1="",""
for i in l:
    s=s+str(i)
l.reverse()
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
        break
    else:
        continue
for i in l:
    s1+=str(i)
s1=s1[::-1]
print(s)
print(s1)




