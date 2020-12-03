
arr = string.split('\n')
arr = [x.split(' ') for x in arr]

#1
right = 0
for line in arr:
  _from, _to = (int(x) for x in line[0].split('-'))
  char = str(line[1][0])
  passw = str(line[2])
  print(_from, _to, char, passw)
  count = 0
  for i in passw:
    if i == char: count += 1
  if count >= _from and count <= _to:
    right += 1

print(right)

#2
right = 0
for line in arr:
  _from, _to = (int(x) for x in line[0].split('-'))
  char = str(line[1][0])
  passw = str(line[2])
  print(_from, _to, char, passw)
  count = 0
  for i in (_from, _to):
    if passw[i-1] == char:
      count += 1
  if count == 1:
    right += 1

print(right)
