s='aaaabbbccddfazz'
a= []
newlist = []
count=0

for i in range(0,len(s)):
    a.append(s[i])
    if len(set(a)) == 1:
        count +=1
        if i == len(s)-1:
            itemcount = a[0] + str(count)
            newlist.append(itemcount)
    elif len(set(a)) > 1:
        itemcount = a[0] + str(count)
        newlist.append(itemcount)
        del a[0:len(a)-1]
        count=1

print(newlist)
newlist2 = ''.join(newlist)

if len(s) < len(newlist2):
    print('Original string was shorter:' + s)
else:
    print('Compressed list is shorter: ' + newlist2)