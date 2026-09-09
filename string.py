# To check for substring 
s1="geeks for geeks"
s2="geeks"
print(s2 in s1)
print(s2 not in s1)
#Concatenation
s1="geeksfor"
s2="geeks"
s3=s1 + s2
print(s3,"welcome to "+s1+s2)
#to check indexing of sub substring
s1="geeksforgeeks"
s2="geeks"
print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2,0,13))
print(s1.index(s2,1,13))
print()
#some operation 
s1="kaggle"
print(s1)
print(len(s1))
s2=s1.upper()
s3=s1.lower()
print(s2)
print(s3)
print(s1.islower())   #it gives true if s1 is in lower case othewise false
print(s1.isupper())   #vice versa
print()
# stars with and ends with parameters
s="geeksforgeeks python course"
print(s.startswith("geeks"))
print(s.endswith("course"))
print(s.startswith("geeks",1))
print(s.startswith("geeks",8,len(s)))
# split and join method
s1="geeks for geeks"
print(s1.split()) #this split is use to convert string into list with comma at space
s2="geeks,for,geeks"
print(s2.split(","))    # in this the comma indicate that "," is to seprate/split at , only
l=["geeksforgeeks","python","course"]
print(" ".join(l))   # this join by space 
print(",".join(l))     # this join by comma ,
#sd strip method
s="_________Geeks___________"
print(s.strip("_"))      #strip used for remove specic varible from string
print(s.lstrip("_"))     #l.strip is used to remove from left side
print(s.rstrip("_"))     #r.strip is used to remove from right side
print()
#find() methods
s1="geeksforgeeks"
s2="geeks"
print(s1.find(s2))
print(s1.find("for"))
print(s1.find(s2,1,len(s1)))
print()
#string comparision
#mainly in depend on order a-z and a>A
s1="geeksforgeeks"
s2="kaggle"
print(s1>s2)
print(s1<s2)        # 'abc'<'ide'
print(s1<=s2)       # 'ABC'<'z'
print(s1>=s2)       # 'ABC'<'abc'
print(s1==s2)       # 'x'>'abcd'
print(s1!=s2)
print()
#pattern searchig
txt= "geeks for geeks"          #or use input
pat="geeks"
pos=txt.find(pat)
while pos>=0:
    print(pos)
    pos= txt.find(pat,pos+1)
print()
#print reverse string
s="geeks"
rev=""
for i in s:
    rev= i + rev
print(rev)
            #short cut method
st="kaggle"
print(str[::-1])
print()
# to check the palindrome
st="abba"
if str==str[::-1] :
    print("Yes")
else :
    print("No")
  # another method
s="abcba"
low=0
high=len(s) - 1
while low<high :
    if s[low] != s[high]:
        print("No")
        break
    low=low+1
    high=high-1
else :
    print("Yes")
print()
#decimal to binary
def DecToBin(b) :
    if b == 0:
        return "0"
    res = ""
    while b>0:
        res= res +(b%2).__str__()    #this is used to convert into string
        b=b//2
    return res[::-1]
print(DecToBin(54))
   #direct method 
def dec_to_bin(n):
    res=bin(n)
    return res[2::]
print(dec_to_bin(46))
