def fun(c):
    
    while(len(c)!=0):
        c=c.replace('()','')
        c=c.replace('[]','')
        c=c.replace('{}','')
        break
        
    if(len(c)==0):
        return True
    else:
        return False
c=input("enter an expression")

print("given string is balanced",fun(c))