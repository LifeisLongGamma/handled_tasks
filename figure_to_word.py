def num_to_word():
	user_input = input('Input a number from 0 to 999 to get its word form: ')
	wnums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	wnums2 = ['', '', '', '', '', '', '', '', '', '', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	wnums3 = ['', '', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	wnums4 = ['', 'hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']

	if len(user_input) == 1:
		index  = int(user_input)
		print(wnums[index])
	elif len(user_input) == 2 and user_input[0] != '1':
		div = []
		for i in user_input:
			div.append(i)
		x, y = int(div[0]), int(div[1])
		if y != 0:
			print(wnums3[x], wnums[y])
		else:
			print(wnums3[x])
	elif len(user_input) == 2 and user_input[0] == '1':
		index1 = int(user_input)
		print(wnums2[index1])
	elif len(user_input) == 3 and user_input[1] != '1':
		div2 = []
		for i in user_input:
			div2.append(i)
		a, b, c = int(div2[0]), int(div2[1]), int(div2[2])
		if c != 0:
			print(wnums4[a], 'and', wnums3[b], wnums[c])
		elif b != 0:
			print(wnums4[a], 'and', wnums3[b])
		else:
			print(wnums4[a])
	elif len(user_input) == 3 and user_input[1] == '1':
		div3 = []
		for i in user_input:
			div3.append(i)
		div4 = [div3[0], ''.join(div3[1:3])]
		m, n = int(div4[0]), int(div4[1])
		print(wnums4[m], 'and', wnums2[n])
	else:
		print('Given number is out of range. Try again.')

print(num_to_word())
		
		
		
