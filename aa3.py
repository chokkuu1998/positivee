mm,nn=map(int,input().split())
ss=list(map(int,input().split()))
if nn==1:
    print(min(ss))
elif nn==2:
    print(max(ss[0],ss[mm-1]))
else:
    print(max(ss))
