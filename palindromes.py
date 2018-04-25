import numpy as np

list1=list(range(100, 1001))
list2=list(range(100, 1001))

c=[]
def multipliers(a,b):
	for i in range(len(a)):
		for j in range(len(b)):
			c.append(a[i]*b[j])
print(c)

def checkpalindrome(a):
	d=str(a)
	return d==d[::-1]

def combined(a,b):
	c.sort()
	for i in c[::-1]:
		if checkpalindrome(i):
			print(i)
			break

multipliers(list1,list2)
combined(list1,list2)



