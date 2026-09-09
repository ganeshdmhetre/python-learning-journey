n=int(input("enter first number:"))
m=int(input("enter second number:"))
small=min(n,m)
for i in range(1,small+1):
    if n % i==0 and m % i==0 :
        gcd=i
print("grest common divisor:",gcd)
