st=sorted(input())

dic={}
for i in st:
    if(i in dic):
        dic[i]+=1
    else:
        dic[i]=1
for k,v in dic.items():
    print(k,end="")
    print(":",end="")
    print(v)
