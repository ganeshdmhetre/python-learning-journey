s1={10,20,30}
print(s1)
s2={20,30,40}
print(s2)
s3={}
print(s3)
print(type(s3))
s4=set()
print(s4)
print(type(s4))
#another exampler code
s={10,20}
print(s)
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update({60,70},[80,90])
print(s)
#another exampler of removal 
s={20,30,40,50}
print(s)
s.discard(30)
print(s)
s.discard(60)
print(s)  # No error shown 
s.remove(40)
print(s)
s.clear()
print(s)
s.update([70,80,90,100])
print(s)
del s # it delete set completely
#finder operators
s={10,20,30,40,50}
print(len(s))
print(40 in s)
print(60 in s)
#operators on two set
s1={10,20,30,40,50}
s2={10,30}
print(s1|s2)
print(s1&s2)
print(s1-s2)
#print(s1 is disjoint (s2))   **# these operator gives us true if their is no common element is present
print(s1 <= s2) #s1 is subset of s2 or not ,if yes it give true
print(s1 > s2) #it gives a proper subset of s2 or not 
print(s1 >= s2) #it gives a superset subset of s2 or not 
print(s1 > s2) #it gives s1 is a proper super set of s2
