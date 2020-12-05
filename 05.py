string = '''<input>'''
string = string.split('\n')

if __name__ == '__main__':
		
	max_row = 0
	max_col = 0
	max_num = 0
	seat_list = []

	for word in string:
		row = 0
		col = 0
		row_start = 0
		row_end = 127
		col_start = 0
		col_end = 7
		for i in range(0,7):
			op = word[i]
			if op == 'F':
				row_end = row_start + (row_end-row_start) // 2
			elif op == 'B':
				row_start = row_start + (row_end-row_start) // 2 + 1
		row = row_start

		for i in range(7,10):
			op = word[i]
			if op == 'L':
				col_end = col_start + (col_end-col_start) // 2
			elif op == 'R':
				col_start = col_start + (col_end-col_start) // 2 + 1
		col = col_start

		seat_nr = row*8+col
		i = 0
		l = len(seat_list)
		while i < l and seat_nr > seat_list[i]: i += 1
		seat_list.insert(i,seat_nr)

		if max_num < row*8+col:
			max_num = row*8+col
			max_row = row
			max_col = col
			max_word = word

	print('highest seat:', word, max_row, max_col, max_num)
	#print(seat_list)

	for i in range(len(seat_list)-1):
		if seat_list[i+1] - seat_list[i] != 1:
			print('my seat:', seat_list[i]+1) 
			break
