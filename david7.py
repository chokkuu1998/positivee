AA,BB=map(int,input().split())
CC=list(map(int,input().split()))
CC=sorted(C)
tt,i=0,0
ff=0
while i<len(C)-2:
  xx,yy,zz=C[i:i+3]
  for j in range(0,B):
    xx,yy,zz=xx+1,yy+1,zz+1 
    if xx<=5 and yy<=5 and z<=5:
      f=1
    else:
      ff=0
  if ff==1:
    tt=t+1
  i=i+3
   
print(tt)
