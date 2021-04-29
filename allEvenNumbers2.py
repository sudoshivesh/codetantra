#AP to print all even numbers of a list using list comprehension
mylist=input("Enter elements seperated by a comma:").split(',')
A=[int(i) for i in mylist]
li=[]
for i in A:
  if i%2==0:
    li.append(i)
print("Even numbers in the list: ",li)
