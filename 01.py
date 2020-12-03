
arr = [int(x) for x in string.split('\n')]

# 1
for i in arr:
  for j in arr:
    if i+j == 2020:
      print(i,j,i+j,i*j)

# 2
for i in arr:
  for j in arr:
    for y in arr:
      if i+j+y == 2020:
        print(i,j,y,i+j+y,i*j*y)

