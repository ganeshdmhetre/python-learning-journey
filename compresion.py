l1=[x for x in range(11) if x % 2 == 0]
print(l1)
l2=[x for x in range(11) if x % 2 != 0]
print(l2)
# in this starting x is a element to add that in the list

# Function to get all the element of the list that are less than x
def getSmaller(l,x):
    l=[e for e in l if e<x]
    return l
print(getSmaller([1,5,7,6,8,6,8,7],5))

#-_____________#
# to get the vowels from the given sting
def getString(s):
    l=[x for x in s if x in "aeiou"]
    return l
print(getString("ganesh_mhetre"))
# to seperate element that start from given character
l2=["ganesh","mhetre","geeks","gfg","gained"]
l3=[x for x in l2 if x.startswith("g")]   
print(l3)
print()
l4=["ganesh","mhetre","geeks","gfg","gained"]
l5=[x.upper() for x in l4 if x.startswith("g")]
print(l5)
#
#
#
#Set Comprehension
l=[10,20,30,40,50,60,3,4,5,6]
s1={x for x in l if x%2==0}
s2={x for x in l if x%2!=0}
print(s1)
print(s2)
#_______#
#Dictonary Comprehension
l1=[1,4,2,3,5,6,7,8]
d1={x:x**3 for x in l1}
print(d1)
d2={x:f"ID[{x}]" for x in range(5)}
print(d2)

# Insert a key where a key becomes value and value becomes key
d1={101:"gfg",102:"ganesh",103,"mhetre"}
d3={v:k for (k,v) in d1.items()}
print(d3)