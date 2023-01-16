

numRows = 4       # add a return statement if numRows==1 return s
s = "paypalishiring"
interval = (numRows-1)*2
output = ""
for i in range(numRows):
    for j in range(i,len(s),interval): #traversing the string for each row (but with intervals)
        output+=s[j]       # this covers almost all the items(and complete first and last row)
        if (i>0 and i<numRows-1 and (interval-(i*2)+j) < len(s) ): # for internal items which decreases by 2 as the row increases.
               output+=s[j+(interval-(i*2))]
print(output)