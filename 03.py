string = '''<input>'''

arr = string.split('\n')
maxc = len(arr[0])
maxr = len(arr)
print(maxc)

prod = 1
for dr, dc in [(1,1),(1,3),(1,5),(1,7),(2,1)]:
  i = j = 0
  trees = 0
  while i < maxr:
    print(arr[i][j])
    if arr[i][j] == '#': trees += 1
    i = i+dr
    j = (j+dc)%maxc
  print('trees:', trees)
  prod *= trees
print("prod:", prod)
