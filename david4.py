ss,kk=map(int,input().split())
if ss>kk:
    ss,kk=kk,ss
list=[]
for i in range(ss):
    mm=list(map(int,input().split()))
    mm.sort()
    li.append(mm)
for j in range(0,k):
    li1=[]
    for i in range(0,s):
        li1.append(li[i][j])
    li1.sort()
    r=0
    for i in range(0,ss):
        list[i][j]=li1[r]
        r=r+1
for i in list:
    print(*i)
