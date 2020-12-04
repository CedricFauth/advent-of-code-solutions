arr = string.split('\n\n')
arr = [x.replace('\n', ' ').split(' ') for x in arr]
correct = 0

for passport in arr:
	values = [False, False, False, False, False, False, False, False]
	for entry in passport:
		sp = entry.split(':',1)
		if len(sp) != 2:
			break
		e,v = sp
		if 'byr' == e:
			if v.isdigit() and len(v) == 4 and int(v) >= 1920 and int(v) <= 2002:
				values[0] = True
		elif 'iyr' == e:
			if v.isdigit() and len(v) == 4 and int(v) >= 2010 and int(v) <= 2020:
				values[1] = True
		elif 'eyr' == e:
			if v.isdigit() and len(v) == 4 and int(v) >= 2020 and int(v) <= 2030:
				values[2] = True
		elif 'hgt' == e:
			sym = v[-2:]
			v = v[:-2]
			if sym == 'cm' and v.isdigit() and int(v) >= 150 and int(v) <= 193:
				values[3] = True
			elif sym == 'in' and v.isdigit() and int(v) >= 59 and int(v) <= 76:
				values[3] = True
		elif 'hcl' == e:
			if v[0] == '#' and len(v) == 7:
				values[4] = True
				for i in v[1:]:
					if not (i >= '0' and i <= '9' or i >= 'a' and i <= 'f'):
						values[4] = False
						break
		elif 'ecl' == e:
			if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				values[5] = True
		elif 'pid' == e:
			if v.isdigit() and len(v) == 9:
				values[6] = True
		elif 'cid' == e:
			values[7] = True
	if all(values[0:7]):
		correct += 1
print(correct)
