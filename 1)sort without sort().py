ln=['c','a','g','s']
for i in range(0,len(ln)):
  for j in range(i+1,len(ln)):
    if ln[i]>ln[j]:
      ln[i],ln[j]=ln[j],ln[i]
print(ln)