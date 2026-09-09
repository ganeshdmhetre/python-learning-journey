# "in" operator for string cheks the whether the given stirng is a substring or not
s="iamthelegend"
print("legend" in s)
print("gend" in s)
#For dictionary checks for key 
d={10:"axy",20:"sdf",30:"gnd"}
print(10 in d)
print(500 not in d)
print()
#for list,tuple,set: check menbership
l=[10,20,30,40,50,]
print(40 in l)
print(50 in l)
print(40 not in l)
print([30,40,] in l) # it is a sub list not the meber of the list
