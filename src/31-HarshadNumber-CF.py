n=int(input())
summ=0
for i in str(n):
    i=int(i)
    summ+=i
if(summ%n==0):
    print(True)
else:
    print(False)
