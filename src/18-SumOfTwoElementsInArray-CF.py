n=int(input())
m=list(map(int,input().split()))
k=int(input())
f=1
arr=[]
for i in range(len(m)):
    for j in range(len(m)):
        if((m[i]+m[j])==k):
            
            f=0
            arr.append([m[i],m[j]])
if(f):
    print("No elements found")
else:
    print(arr[0][0],arr[0][1])
