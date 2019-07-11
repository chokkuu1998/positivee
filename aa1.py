aain,bb=input().split()
aain=int(ain)
bb=int(b)
ss=''
uu=2
if(aain+bb<=3):
    for i in range(0,aain+bb):
        if(i%2!=0):
            s=s+'0'
        else:
            s=s+'1'
else:    
    for i in range(0,aain+bb):
        if(i==uu):
            s=s+'0'
            if(u==bb):
                u=uu+2
            else:
                u=uu+3
        else:
            s=s+'1'
x=len(s)-1
if(int(s[x])==0):
    print('-1')
elif aain==1 and bb==2: 
     print("011")
else:
    print(s)
