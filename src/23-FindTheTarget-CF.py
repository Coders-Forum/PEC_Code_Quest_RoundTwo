n=int(input())
target=int(input())
arr=[]
for _ in range(n):
    x=int(input())
    arr.append(x)
    
for i in arr:
    x=target-i
    if(x in arr):
        print(arr.index(i))
        print(arr.index(x))
        break
