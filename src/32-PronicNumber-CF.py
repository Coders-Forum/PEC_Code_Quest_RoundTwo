s=int(input())
e=int(input())
x=0
i=0
while(True):
    x=i*(i+1)
    if(x>e):
        break
    if(x>=s):
        print(x)
    
    i+=1
    
