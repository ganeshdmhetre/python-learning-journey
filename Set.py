#________________________#
#set fuction
#distinct elements # Unordered # No indexing in these # Union Intesection
#uses hashing inertnally
s1={10,20,30,40}
print(s1)
s2=set([10,20,30])
print(s2)
print(type(s2))
s3={}
print(s3)
s4= set()    #empty set
print(s4)
print(type(s4))
#Incertion operation
s={10,20}
print(s)
s.add(30)
print(s)
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update([60,70],[80,90])
print(s)
#Removal operation
s={10,20,30,40,50,60,70}
s.discard(30)              #if the element is not present then it's ok 
s.remove(20)               # if the element is not present then raise an error
print(s)
s.clear()                  # clear the set elements only but it leaves an empty set, so there after add function works 
print(s)
s.add(40)
print(s)
del(s)                    #it clears the set it self after printing the set shows an error

#_Operation of two set
s1={2,4,6,8}
s2={3,6,9,4}
print(s1|s2)
print(s1.union(s2))
print(s1&s2)
print(s1.intersection(s2))
print(s1-s2)
print(s1.difference(s2))
print(s1^s2)
print(s1.symmetric_difference(s2))

print(s1.isdisjoint(s2))
print(s1<=s2)
print(s1.issubset(s2))
print(s1<s2)
print(s1>=s2)
print(s1.issuperset(s2))
print(s1>s2)




