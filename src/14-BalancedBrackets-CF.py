n=input()
s=[]
f=1
st={"]":"[","}" :"{",")" :"("}
for i in n:
    if(not i.isalpha()):
        if(i in st):
            x=s.pop()
           
            if(x!=st[i]):
                f=0
                break
                
        else:
            s.append(i)
print(f)
