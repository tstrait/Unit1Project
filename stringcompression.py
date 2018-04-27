mystring = 'abbbcccdddde'

def string_compression(mystring):
    print("Original string:", mystring)
    a=[]
    compressed=[]
    #for each character in string, check if next character is the same or not
    for i in range(0,len(mystring)-1):
        #if next character is the same, add to a temporary string
        if mystring[i] == mystring[i+1]:
            a.append(mystring[i+1])
        #if not, add current character and count the length of group of same characters; add that to the compressedstring list
        else:
            a.append(mystring[i])
            compresseditem = a[0] + str(len(a))
            compressed.append(compresseditem)
            a=[]
    #add the last character
    a.append(mystring[-1:])
    compresseditem = a[0] + str(len(a))
    compressed.append(compresseditem)
    #join list elements into a compressed string
    compressedstring = ''.join(compressed)
    #only return compressed version if it's shorter than original string
    if len(compressedstring) >= len(mystring):
        print("Original string is shorter than compressed:", mystring)
    else:
        print("Compressed string:", compressedstring)
    
string_compression(mystring)