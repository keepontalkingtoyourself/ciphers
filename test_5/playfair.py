def cipher(Matrix, char1, char2):
	idx1 = Matrix.index(char1)
	idx2 = Matrix.index(char2)
	idxs1 = [idx1//6, idx1%6]
	idxs2 = [idx2//6, idx2%6]
	
	if idxs1[0] == idxs2[0]:
		res1 = [idxs1[0], (idxs1[1]+1)%6]
		res2 = [idxs2[0], (idxs2[1]+1)%6]
	elif idxs1[1] == idxs2[1]:
		res1 = [(idxs1[0]+1)%6, idxs1[1]]
		res2 = [(idxs2[0]+1)%6, idxs2[1]]
	else:
		if idxs1[0] < idxs2[0] and idxs1[1] < idxs2[1]:
			res1 = [idxs1[0], idxs2[1]]
			res2 = [idxs2[0], idxs1[1]]
		elif idxs1[0] > idxs2[0] and idxs1[1] < idxs2[1]:
			res1 = [idxs2[0], idxs1[1]]
			res2 = [idxs1[0], idxs2[1]]
		elif idxs1[0] < idxs2[0] and idxs1[1] > idxs2[1]:
			res1 = [idxs2[0], idxs1[1]]
			res2 = [idxs1[0], idxs2[1]]
		else:
			res1 = [idxs1[0], idxs2[1]]
			res2 = [idxs2[0], idxs1[1]]
	
	return res1, res2

def main():
	Alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,'
	Alphabet = list(Alphabet)
	Matrix = []
	text, key = input().split(' ')
	key = list(key)
	ciphertext = ''
	
	for el in key:
		if el in Alphabet:
			Matrix.append(el)
			Alphabet.remove(el)
	Matrix.extend(Alphabet)
	# print(Matrix)
	
	l = len(text)
		
	for i in range(0, l-1, 2):
		char1, char2 = text[i], text[i+1]
	
		if char1 == char2:
			text = text[:i+1] + 'Ъ' + text[i+1:]
			char2 = 'Ъ'
	
		res1, res2 = cipher(Matrix, char1, char2)
		
		ciphertext += Matrix[res1[0]*6 + res1[1]]
		ciphertext += Matrix[res2[0]*6 + res2[1]]
		
	if len(text)%2 != 0:
		res1, res2 = cipher(Matrix, text[-1], 'Ъ')
		ciphertext += Matrix[res1[0]*6 + res1[1]]
		ciphertext += Matrix[res2[0]*6 + res2[1]]
	
	print(ciphertext)

if __name__ == '__main__':
	main()
