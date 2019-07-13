ss1,kk1=map(int,input().split())
if ss1>k1:
    ss1,k1=k1,s1
list2=[]
for i in range(s1):
    mm1=list(map(int,input().split()))
    mm1.sort()
    list2.append(m1)
for j in range(0,kk1):
    li1=[]
    for i in range(0,s1):
        li1.append(li2[i][j])
    li1.sort()
    r1=0
    for i in range(0,ss1):
        list2[i][j]=li1[r1]
        r1=r1+1
for i in list2:
    print(*i)
