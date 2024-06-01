n=int(input())
m=list(map(int,input().split()))
k=int(input())
a=m[0:k]
b=m[k::]
c=b+a
for i in c:
    print(i,end=" ")

    
