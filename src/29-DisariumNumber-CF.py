n=int(input())
res=0
j=1
for i in str(n):
    a=int(i)**j
    res+=a
    j+=1
print(res==n)
