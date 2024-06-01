def timeConversion(s):
    n=int(s[:2])
    
    if(s[-2::])=="PM":    
        if(s[:2]=='12'):
            return("12"+""+s[2:8])
        else:
            n=str(n+12)
            return(n+""+s[2:8])
      
    elif(s[-2::])=="AM":
        print(s[:2])
        if(s[:2]=='12'):
            return("00"+""+s[2:8])
        elif(int(s[:2])<12):
            return(s[:8])
        else:
            n=str(n+12)
            return(n+""+s[2:8])
