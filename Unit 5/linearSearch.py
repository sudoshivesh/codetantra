#To write a python program linear search. 
mylist=input("Enter the list of numbers: ").split()
a=[int(i) for i in mmylist]
length=len(A)
value=int(input("The number to search for: "))
loc=-1
for i in range(length):
  if value==A[i]:
    loc=i+1
    break
if loc==-1:
  print(value,"was not found.")
else:
  print(value,"was found at index",str(loc-1)+'.')
  
