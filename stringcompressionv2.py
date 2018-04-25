s='aaaabbbccddfaz'
a= []
newlist = []
count=0

for i in range(0,len(s)):
    a.append(s[i])
    if len(set(a)) == 1:
        count +=1
    elif len(set(a)) > 1:
        itemcount = a[0] + str(count)
        newlist.append(itemcount)
        del a[0:len(a)-1]
        count=1
    if i == len(s)-1:
        if len(set(a)) > 1:
            del a[0:len(a) -1]
            itemcount = a[0] + str(count)
            newlist.append(itemcount)
        else: 
            itemcount = a[0] + str(count)
            newlist.append(itemcount)

newlist2 = ''.join(newlist)

print('Original String:' + s)
if len(s) < len(newlist2):
    print('Original string is shorter: ' + s)
else:
    print('Compressed string is shorter: ' + newlist2)
