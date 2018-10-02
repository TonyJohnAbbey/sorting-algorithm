l = [float(x) for x in input("Enter a list of elements: \n").split()]
f = []
for i in range(len(l)):
	for j in range(len(f)):
		if l[i] < f[j]:
			f.insert(j, l[i])
			break
	else:
		f.append(l[i])
	print(f)