l=[10,20,30,40]
print(l)
print(l[-1])
print(l[3])
print(l[0])
print(l[-2])
l=[10,20,30,40,50,60,70,80,90]
l.append(30)       # add at the end of the list
print(l)
l.insert(1,15)    # add 15 at 1 postion
print(l)
print(15 in l)    # check if their is 15 in list l 
print(l.count(30))   # to count the no. of elements
print(l.index(30))   # position of 30 first acurance
print(l.index(30,4)) # position of thirty from 4 to len(l)
print()
#_____________#
#to demonstrate removal of item 
l=[10,20,30,40,50,60,70,80,90]
print(l)
l.remove(20)
print(l)
print(l.pop())   # it remove last element of the list and pop the element
print(l)
print(l.pop(2))  # we can also use indexing in to remove specific element
print(l)
del l[1]        
print(l)
print(l)
del l[0:2]
print(l)
#_____________-# 
#Some Genreal purpose language
l=[40,50,20,30]
print(max(l))
print(min(l))
print(len(l))
print(sum(l))
l.reverse()    # this rverse string and store at the loction of pre existing list memory location
print(l)
l.sort()       # sort means arange it int the right order 
print(l)
print()
#____________#
#SLICING
l=[10,20,30,40,50,60,70,80,90]
print(l[0:5:2])                   #l[start:stop:step]
print(l[:4])
print(l[2:])
print(l[4:1:-1])
print(l[-1:-5:-1])
print(l[::-1])            # use to print the reverse list
print(l[:])                # use to pritn the hole list
l1=[10,20,30,40]
l2=l1[:]                  # here l1 and l2 contian same elements but their is diff memory location
t1=(10,20,30)
t2=t1[:]                  # here in tuple both contain same elements and location
s="geeks"
s1=s[:]
print(s1,t2,l2)
#___________________#
#Get Smaller Element from the list
def getSmaller(l,x):
    res=[]
    for e in l:
        if e < x :
            res.append(e)
    return res
#_________________#
#Seperate Even and Odd elemnt from the list
def getEvenOdd(l):
    even=[]
    odd=[]
    for i in l :
        if i % 2 ==0 :
            even.append(i)
        else :
            odd.append(i)
    return even,odd

