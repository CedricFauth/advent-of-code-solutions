string = '''<input>'''

# 1

arr = string.split('\n\n')
arr = [x.replace('\n','') for x in arr]

l = list()
for group in arr:
	s = set(group)
	l.append(s)

print(sum((sum((1 for _ in g)) for g in l)))


# 2

arr = string.split('\n\n')
arr = [x.split('\n') for x in arr]
print(arr)

l = list()
for group in arr:
	s = set(group[0])
	for person in group:
		s = s & set(person)
	l.append(s)

print(sum((sum((1 for _ in g)) for g in l)))
