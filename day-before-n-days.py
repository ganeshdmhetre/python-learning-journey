print("d |" \
"       0=sunday" \
"       1=monday" \
"       2=tuesday" \
"       3=wednesday" \
"       4=thursday" \
"       5=friday" \
"       6=saturday" \
"       7=saunday")
d=int(input("enter d:"))
n=int(input("enter n:"))
print((d-n)%10)