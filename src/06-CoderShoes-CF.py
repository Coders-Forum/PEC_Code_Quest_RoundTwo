n,m=map(int,input().split())


if(n<m):
    right=n
    print(right)
else:
    right=n
    left=right-m
    print(right+left)
