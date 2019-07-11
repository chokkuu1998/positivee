xx=input()
ff=0
alphaa="abcdefghijklmnopqrstuvwxyz"
for i in alphaa:
  if i  not in xx.lower():
    ff=1
if ff==1:
  print("no")
else:
  print("yes")
