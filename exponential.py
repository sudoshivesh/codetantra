#WAP to compute the exponential of number w.r.t. another number.
def expo(base,exponent):
  return base**exponent
num1=int(input("Enter Base Number "))
num2=int(input("Enter Exponent Number "))
print(num1,'^',num2,'=',expo(num1,num2))
