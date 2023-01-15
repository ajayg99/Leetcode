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