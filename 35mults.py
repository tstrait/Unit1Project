a=[]
b=[]

for i in range(0,10):
	if i%3 == 0:
		a.append(i)
	elif i%5 == 0:
		a.append(i)

print(sum(a))