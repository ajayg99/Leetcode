s = 'abcabcbb'

l = 0  #left pointer
r = 0  #right pointer
result = 0 #result length
seen = set()  #set to hold seen values

for r in range(0,len(s)): # increment right pointer
    while s[r] in seen: # if right pointer in set, delete the value of right pointer in set and increment left pointer
        seen.remove(s[l])
        l+=1
    result = max(result,r-l+1) # else find the length 
    seen.add(s[r])

print(result)


#Approach 2

s = 'abcabcbb'
temp = set()
res = 0
for i in range(0,len(s)):  #loop for all the element
    for j in range(i,len(s)): #loop for each element starting for its position
        if s[j] in temp: #if s[j] is in temp (duplicate)
            res = max(res,len(temp)) # the temp contains all the non duplicate elements, hence take the len 
            temp = set() # re initailize temp
            break # break the inner loop -> i+=1
        else:
            temp.add(s[j]) #else add the value to the set
res = max(res,len(temp)) #if the string contains no duplicate 
print(res)