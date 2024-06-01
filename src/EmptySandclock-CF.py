n=int(input())

#Upper part
for i in range(1,n//2+1):
    print("*"*i," "*(n-(2*i)-1),"*"*i)

#Middle part
print("*"*(n+1))

#Lower part
for i in range(n//2,-1,-1):
    print("*"*i," "*(n-(2*i)-1),"*"*i)
