aa,bb=map(int,input().split())
cc,dd=map(int,input().split())
ee,ff=map(int,input().split())
gg,hh=map(int,input().split())
if(abs((aa-cc)==(gg-ee))==abs((bb-hh)==(dd-ff))):
    print("yes")
else:
    print("no")
