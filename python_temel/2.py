# github.com/echtr

liste = [[1, 2], [3, 4], [5, 6, 7]]
liste.reverse()
for i in liste:
	if type(i) == list:
		i.reverse()
print(liste)