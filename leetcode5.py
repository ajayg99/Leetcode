def substring(s):          # function to retrive all the substrings
    temp = ''
    op = []
    for i in range(len(s)-1): 
        temp+=s[i]
        for j in range(i+1,len(s)):
            temp+=s[j]  
            op.append(temp)
        temp = ""
    return op

def check(palin):  #checking plaindrome for each substring
    res = ''
    maxi = 0
    for i in palin:
        l = 0
        r = len(i)-1
        for j in range(0,len(i)):
            if i[l]==i[r]:
                l+=1
                r-=1
            else:
                break
            if r==-1:
                if maxi<len(i):
                    maxi = len(i)
                    res = i
    return res

# OPTIMIZED

def sliding_window(s):
    r_ans = 0
    l_ans = 0
    maxi = 0
    # palindrome with odd length
    for i in range(0,len(s)):
        l,r = i,i # for each value of i checking for plaindrome from middle 
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (maxi<(r-l+1)):
                maxi = r-l+1
                r_ans = r
                l_ans = l
            l-=1
            r+=1
        # palindrome with even length
        l,r = i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (maxi<(r-l+1)):
                maxi = r-l+1
                r_ans = r
                l_ans = l
            l-=1
            r+=1
    return s[l_ans:r_ans+1]
#optimized
s='babadbbbb'
print(sliding_window(s))
#bruteforce
op = substring(s)
print(check(op))