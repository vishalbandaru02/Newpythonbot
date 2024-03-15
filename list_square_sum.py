#sum of squares of the list
a = list(map(int, input("enter the list:").split()))
print(a)
l=[]
for i in a:
    s=i*i
    l.append(s)
print(l)
d=sum(l)
print(d)
