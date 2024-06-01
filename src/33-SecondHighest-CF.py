n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
k=sorted(a)

print(k[-2])
