x=int(input())
m=list(map(int,input().split()))
mi=min(m)
ma=max(m)
f=1
for i in range(mi,ma+1):
    if(i not in m):
        f=0
        print(i,end=" ")
if(f):
    print("All elements are present")
