i=1
while i < 6:
  print(i)
  i += 1    

#with break statement,we can stop the loop even if the while condition is true
j=1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1

  #with continue statement,we can stop the current iteration, and continue with the next
k=0
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)