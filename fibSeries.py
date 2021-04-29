#WAP to compute the sum of Fibonacci series up to nth term.
n=int(input("Enter number of terms "))
t1,t2=-1,1
sumt=0
for i in range(1,n+1):
  nextTerm=t1+t2
  sumt=sumt+nextTerm
  t1=t2
  t2=nextTerm
print("Sum of Fibonacci series upto ",n,"th terms",sumt)
