# github.com/echtr

yeni = []
def duzlestir(islem):
	for i in islem:
		if isinstance(i, list): duzlestir(i)
		else: yeni.append(i)
	return yeni


liste = [[[1,2,3],[4,5,6],"a"],[[14,25,36]],[["cat"],["dog"]]]
print(duzlestir(liste))
