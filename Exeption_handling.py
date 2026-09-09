try:
    x=0
    print(x/0)
except:
    print("error ocured")

# With specific errors
try:
    x=0
    print(x/0)
except ZeroDivisionError:
    print("zero is in the divisor")
except:
    print("Unknown Error")

#with another form
try:
    num1,num2=10,0
    print(int(3.14))
except ZeroDivisionError as zde:
    print(zde)
except Exception as e :
    print(e)
else:
    print('Everything is fine')
finally:
    print("Program is end!")