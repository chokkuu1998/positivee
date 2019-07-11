tthi = int(input())
aaa1 = list(map(int,input().split()))
sss,l = 0,[]
bb1 = [x for x in range(1,tthi+1)]
for i in aaa1:
  if i in bb1:
    bb1.remove(i)
kh = 0
for i in range(0,tthi-1):
  p = aaa1[i]
  for j in range(i+1,thi):
    if p == aaa1[j]:
      if p < b1[kh]:
        aaa1[j] = bb1[kh]
        sss += 1
      else:
        aaa1[i] = bb1[kh]
        sss += 1
      kh += 1
print(sss)
print(*aaa1)
