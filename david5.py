NN,k=map(int,input().split())
ll=list(map(int,input().split()))
cc=0
for i in range(0,len(l)):
    if (ll[i]+k)<=5:
        cc=cc+1
print(cc//3)
