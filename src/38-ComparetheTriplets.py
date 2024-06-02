def compareTriplets(a, b):
    x=0
    y=0
    for i in range(3):
        if(a[i]>b[i]):
            x+=1
        elif(a[i]<b[i]):
            y+=1
    return (x,y)
