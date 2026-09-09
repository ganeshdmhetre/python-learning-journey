# To Find Average Or Mean of a List
def getmean(l):
    sum=0
    for i in l:
        sum=sum+i
    n=len(l)
    avg=sum/n
    return avg
print(getmean([10,2,30,40,4,6,7]))
print()
#___________#
#count distict element int a list
def distict(l):
    res=1
    for i in range(1,len(l)):
        if l[i] in l[0:i]:
            res=res+1
    return res
l=[10,2,30,40,8,6,9,4,6,7]
print(distict(l))
#______________#
#check if the list is sorted or not
def isSorted(l):
    i=1
    while i<len(l):
        if l[i] < l[i-1]:
            return False
        i=i+1
    return True
l1=[1,2,3,4,5]
l2=[3,5,6,4,7,5,]
print(isSorted(l1))
print(isSorted(l2))
# use Sored function
def Sorted(l):                          
    sl=sorted(l)        # Diff b/w sort and sorted 
    if l == sl :         # sort just sort the list and store at same memory location
        return True       # sorted create a new list which is sorted 
    else :                 # same for reverse and reversed for list
        return False       # l.reverse() and l.reversed  & l.sort() and l.sorted()
print(Sorted(l2))
print(Sorted(l1))
    