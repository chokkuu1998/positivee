tte=input()
dum=0
for i in range(0,len(tte)-1):
  for j in range(i+1,len(tte)):
    if tte[i]<tte[j]:
      dum=1
      print(tte[j:])
      break
  if dum==1:
    break
  else:
    print(tte)
