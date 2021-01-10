n=int(input("ENTER THE LIST SIZE: "))
t=[]
for i in range(0,n):
  print("ENTER THE LIST ELEMENTS SEPERATED BY A SPACE ")
  x=input().split()
  for i in range(0,len(x)):
    x[i]=int(x[i])
  t.append(list(x))
for i in range(0,len(t)):
  for j in range(0,len(t)-i-1):
    if(t[j][1]>t[j+1][1]):
      temp=t[j]
      t[j]=t[j+1]
      t[j+1]=temp
print("the new list order is :")
print(t)