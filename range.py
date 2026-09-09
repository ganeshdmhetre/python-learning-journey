r=range(5)
print(r)
l=list(r)
print(l)              # in range the starts for zero and ends at given digit minus 1 
print(type(l))        # here we give the digit 5 so it starts for 0 and ends at (5-1) 4
print(type(r))
#Range with two paramerters
r=range(1,11)
print(r)           # i this we tell to form where to start and to where stop 
l=list(r)          # it stop minus one of last digit
print(l)
#Range with three parameters
r=range(10,20,2)      #(x,y,z)
l=list(r)      # in this first number is starting and second is ending and another is to add the afer every digit
print(r) 
#
r=range(20,10,-2)  #(x,y,z)
l=list(r)    # if er provide negative number then we get output even through the numbers are grater than y
print(r)      #it stops when it is samller than or equal to y