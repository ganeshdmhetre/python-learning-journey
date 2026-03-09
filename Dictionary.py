#in dictonary their are key value pair 
d={1:'abc' , 2:'gfg' , 3:'xyz'}
print(d)
d={}
d['laptop']=100000
d['mobile']=20000
d['earphone']=1500
print(d['mobile'])
print(d)
#operaation to get value from the key
d={10:'geeks',20:'hush',30:'abc'}
print(d)
print(d.get(10))
print(d.get(125))
print(d.get(19,'NA'))
#IMP operation
d={100:'m2',101:'phycis',103:'pps'}
d[102]='mechanics'
print(len(d))
print(d.pop(102))
print(d)
del d[103]
print(d)
d[104]='electronics'
print(d)
d[105]='iks'
print(d.popitem())
print(d)

