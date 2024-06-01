m=int(input())
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
f=1
for i in a:
    for j in b:
        if(i==j):
            f=0
            x.append(i)
if(f):
    print("No common elements")
else:
    for i in x:
        print(i,end=" ")


#OR

'''
m=int(input())
n=int(input())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
k=(list(a&b))
if(len(k)==0):
    print("No common elements")
else:
    for i in k:
        print(i,end=" ")

'''
